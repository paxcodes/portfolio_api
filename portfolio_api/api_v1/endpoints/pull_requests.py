from fastapi import APIRouter

router = APIRouter()


@router.get("/featured")
def read_pull_requests():
    return {"msg": "Featured PRs coming soon"}
