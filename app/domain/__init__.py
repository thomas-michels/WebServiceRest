from fastapi import APIRouter

# Importar endpoints
from app.domain.views.users_view import router as user_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["users"])
