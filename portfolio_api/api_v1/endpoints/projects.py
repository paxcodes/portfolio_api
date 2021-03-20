from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_projects():
    return {"msg": "Projects coming soon"}
