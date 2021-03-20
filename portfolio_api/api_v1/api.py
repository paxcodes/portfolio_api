from fastapi import APIRouter

from .endpoints import projects, pull_requests

api_router = APIRouter()

api_router.include_router(
    pull_requests.router, prefix="/pull-requests", tags=["Pull Requests"]
)
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
