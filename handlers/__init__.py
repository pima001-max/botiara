from .user.menu import router
from .common import common_router
from .admin import admin_router
from .user import user_router


# Экспортируем список маршрутизаторов.
__all__ = ["common_router", "admin_router", "user_router", "router"]
