import datetime
import uuid
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
    JSON,
    Enum,
)
from sqlalchemy.orm import relationship
from backend.database.session import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

# ==========================================
# Multi-Tenancy & Access Control
# ==========================================
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    plan = Column(String(50), default="enterprise")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    users = relationship("User", back_populates="organization", cascade="all, delete-orphan")
    customers = relationship("Customer", back_populates="organization", cascade="all, delete-orphan")
    insights = relationship("Insight", back_populates="organization", cascade="all, delete-orphan")

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    role = Column(String(50), default="analyst")  # admin, executive, manager, analyst, viewer
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    organization = relationship("Organization", back_populates="users")
    audit_logs = relationship("AuditLog", back_populates="user")

# ==========================================
# Business Domain Entities
# ==========================================
class Customer(Base):
    __tablename__ = "customers"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    plan = Column(String(50), default="standard")
    arr = Column(Float, default=0.0)  # Annual Recurring Revenue
    health_score = Column(Integer, default=85)  # 0 to 100
    churn_probability = Column(Float, default=0.05)  # 0.0 to 1.0
    usage_trend = Column(Float, default=0.0)  # e.g., -24.0%
    support_ticket_count = Column(Integer, default=0)
    status = Column(String(50), default="active")  # active, at_risk, churned
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    organization = relationship("Organization", back_populates="customers")

class Lead(Base):
    __tablename__ = "leads"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    company_name = Column(String(255), nullable=False)
    contact_name = Column(String(255), nullable=True)
    contact_email = Column(String(255), nullable=True)
    score = Column(Integer, default=50)  # 0 to 100
    pipeline_stage = Column(String(50), default="qualified")
    deal_value = Column(Float, default=10000.0)
    scoring_factors = Column(JSON, default=list)  # list of reasons/factors
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    customer_id = Column(String(36), ForeignKey("customers.id"), nullable=True)
    subject = Column(String(255), nullable=False)
    category = Column(String(100), default="General")  # Payment, Login, API, Performance
    priority = Column(String(50), default="medium")
    root_cause = Column(Text, nullable=True)
    estimated_revenue_risk = Column(Float, default=0.0)
    status = Column(String(50), default="open")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# ==========================================
# AI Business Intelligence & Human-in-the-Loop
# ==========================================
class Insight(Base):
    __tablename__ = "insights"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    type = Column(String(50), nullable=False)  # CHURN_RISK, REVENUE_OPPORTUNITY, ANOMALY, SUPPORT_SPIKE
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(20), default="HIGH")  # CRITICAL, HIGH, MEDIUM, LOW
    metric_impact = Column(String(255), nullable=True)  # e.g., "$184K ARR at risk"
    metadata_json = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    organization = relationship("Organization", back_populates="insights")
    recommendations = relationship("Recommendation", back_populates="insight", cascade="all, delete-orphan")

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    insight_id = Column(String(36), ForeignKey("insights.id"), nullable=True)
    title = Column(String(255), nullable=False)
    recommended_action = Column(Text, nullable=False)
    expected_impact = Column(String(255), nullable=False)
    risk_level = Column(String(50), default="LOW")  # LOW, MEDIUM, HIGH (High requires human approval)
    status = Column(String(50), default="pending")  # pending, approved, dismissed, executed
    action_type = Column(String(100), default="crm_task")  # crm_task, slack_alert, email_outreach, n8n_trigger
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    insight = relationship("Insight", back_populates="recommendations")

class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    agent_name = Column(String(100), nullable=False)  # Orchestrator, DataAgent, StrategyAgent
    prompt = Column(Text, nullable=False)
    output = Column(Text, nullable=True)
    status = Column(String(50), default="completed")  # running, completed, failed
    latency_ms = Column(Integer, default=0)
    token_usage = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# ==========================================
# Enterprise Security & Audit
# ==========================================
class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False)  # USER_LOGIN, APPROVE_ACTION, QUERY_COPILOT, EXPORT_DATA
    resource_type = Column(String(100), nullable=True)
    resource_id = Column(String(100), nullable=True)
    details = Column(JSON, default=dict)
    ip_address = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")
