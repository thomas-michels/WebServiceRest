from fastapi import FastAPI
from settings import PROJECT_NAME, BACKEND_CORS_ORIGINS
from starlette.middleware.cors import CORSMiddleware
from app.domain import api_router
from app.domain.models import users, sales, orders, products
from database import engine
from starlette.responses import RedirectResponse

users.Base.metadata.create_all(bind=engine)
sales.Base.metadata.create_all(bind=engine)
orders.Base.metadata.create_all(bind=engine)
products.Base.metadata.create_all(bind=engine)

app = FastAPI(title=PROJECT_NAME)

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")

app.include_router(api_router)
