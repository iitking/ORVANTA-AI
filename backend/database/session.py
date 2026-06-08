import asyncio
from typing import AsyncGenerator
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.config import settings

Base = declarative_base()

# Determine if aiosqlite is available when SQLite is specified
use_native_async = True
if "sqlite" in settings.DATABASE_URL:
    try:
        import aiosqlite  # noqa: F401
    except ImportError:
        use_native_async = False

if use_native_async:
    try:
        from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

        engine = create_async_engine(
            settings.DATABASE_URL,
            echo=False,
            future=True,
        )

        AsyncSessionLocal = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

        async def get_db() -> AsyncGenerator[AsyncSession, None]:
            """Dependency providing native asynchronous session."""
            async with AsyncSessionLocal() as session:
                try:
                    yield session
                finally:
                    await session.close()

        async def init_db():
            """Initialize database tables with native async engine."""
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

    except Exception:
        use_native_async = False

if not use_native_async:
    # Graceful fallback: use standard synchronous SQLite with thread-wrapped async session
    from sqlalchemy import create_engine

    # Convert sqlite+aiosqlite URL to standard sqlite URL
    sync_url = settings.DATABASE_URL.replace("sqlite+aiosqlite://", "sqlite://")
    sync_engine = create_engine(sync_url, connect_args={"check_same_thread": False})
    SyncSessionLocal = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False)

    class AsyncSessionWrapper:
        """Wraps synchronous SQLAlchemy Session to provide async/await compatibility."""
        def __init__(self, sync_session):
            self._sync_session = sync_session

        async def execute(self, statement, *args, **kwargs):
            return await asyncio.to_thread(self._sync_session.execute, statement, *args, **kwargs)

        def add(self, instance):
            self._sync_session.add(instance)

        async def commit(self):
            await asyncio.to_thread(self._sync_session.commit)

        async def flush(self):
            await asyncio.to_thread(self._sync_session.flush)

        async def rollback(self):
            await asyncio.to_thread(self._sync_session.rollback)

        async def close(self):
            await asyncio.to_thread(self._sync_session.close)

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                await self.rollback()
            await self.close()

    async def get_db():
        """Dependency providing thread-wrapped async session for standard SQLite."""
        sync_sess = SyncSessionLocal()
        wrapper = AsyncSessionWrapper(sync_sess)
        try:
            yield wrapper
        finally:
            await wrapper.close()

    async def init_db():
        """Initialize database tables using standard synchronous SQLite engine."""
        await asyncio.to_thread(Base.metadata.create_all, sync_engine)
