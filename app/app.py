from fastapi import FastAPI
from settings import PROJECT_NAME, BACKEND_CORS_ORIGINS
from starlette.middleware.cors import CORSMiddleware
from app.domain import api_router

app = FastAPI(title=PROJECT_NAME)

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
