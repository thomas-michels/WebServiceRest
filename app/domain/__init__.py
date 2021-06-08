from fastapi import APIRouter

# Importar endpoints
from app.domain.views.users_view import router as user_router
from app.domain.views.sales_view import router as sale_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(sale_router, prefix="/sales", tags=["sales"])
