from enum import Enum
from typing import List, Set

class Role(str, Enum):
    ADMIN = "admin"
    EXECUTIVE = "executive"
    MANAGER = "manager"
    ANALYST = "analyst"
    VIEWER = "viewer"

class Permission(str, Enum):
    VIEW_DASHBOARD = "view_dashboard"
    QUERY_COPILOT = "query_copilot"
    EXECUTE_ANALYTICS = "execute_analytics"
    APPROVE_ACTIONS = "approve_actions"
    MANAGE_USERS = "manage_users"
    MANAGE_INTEGRATIONS = "manage_integrations"
    CONFIGURE_GUARDRAILS = "configure_guardrails"

ROLE_PERMISSIONS = {
    Role.ADMIN: {
        Permission.VIEW_DASHBOARD,
        Permission.QUERY_COPILOT,
        Permission.EXECUTE_ANALYTICS,
        Permission.APPROVE_ACTIONS,
        Permission.MANAGE_USERS,
        Permission.MANAGE_INTEGRATIONS,
        Permission.CONFIGURE_GUARDRAILS,
    },
    Role.EXECUTIVE: {
        Permission.VIEW_DASHBOARD,
        Permission.QUERY_COPILOT,
        Permission.EXECUTE_ANALYTICS,
        Permission.APPROVE_ACTIONS,
    },
    Role.MANAGER: {
        Permission.VIEW_DASHBOARD,
        Permission.QUERY_COPILOT,
        Permission.EXECUTE_ANALYTICS,
        Permission.APPROVE_ACTIONS,
    },
    Role.ANALYST: {
        Permission.VIEW_DASHBOARD,
        Permission.QUERY_COPILOT,
        Permission.EXECUTE_ANALYTICS,
    },
    Role.VIEWER: {
        Permission.VIEW_DASHBOARD,
    },
}

def has_permission(role: str, permission: Permission) -> bool:
    try:
        r = Role(role)
        return permission in ROLE_PERMISSIONS.get(r, set())
    except ValueError:
        return False
