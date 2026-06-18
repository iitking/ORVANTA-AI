import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.database.session import init_db
from backend.api.auth import router as auth_router
from backend.api.dashboard import router as dashboard_router
from backend.api.copilot import router as copilot_router
from backend.api.inbox import router as inbox_router
from backend.api.integrations import router as integrations_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize database tables
    try:
        await init_db()
    except Exception as e:
        print(f"Database initialization notice: {e}")
    yield
    # Shutdown

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Autonomous B2B Business Intelligence & Growth Platform API",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Timing & Audit Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time-Sec"] = f"{process_time:.4f}"
    return response

# Register Routers
app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
app.include_router(dashboard_router, prefix=settings.API_V1_PREFIX)
app.include_router(copilot_router, prefix=settings.API_V1_PREFIX)
app.include_router(inbox_router, prefix=settings.API_V1_PREFIX)
app.include_router(integrations_router, prefix=settings.API_V1_PREFIX)

from fastapi.responses import HTMLResponse
from backend.web_ui import get_portal_html

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "ai_engine": "online",
        "multi_agent_orchestrator": "ready"
    }

@app.get("/", response_class=HTMLResponse)
@app.get("/dashboard", response_class=HTMLResponse)
async def root():
    """Serves the interactive ORVANTA AI Executive Dashboard & Copilot Web UI."""
    return HTMLResponse(content=get_portal_html(), status_code=200)

@app.get("/api")
async def api_info():
    return {
        "platform": settings.PROJECT_NAME,
        "tagline": "Turn business data into decisions, decisions into actions, and actions into measurable growth.",
        "documentation": "/docs",
        "health": "/health",
        "ui": "/"
    }
