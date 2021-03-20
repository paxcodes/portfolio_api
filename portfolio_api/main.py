from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api_v1.api import api_router
from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
)


@app.get("/")
async def home():
    return {"msg": "Hello World"}


app.include_router(api_router, prefix=settings.API_V1_STR)
