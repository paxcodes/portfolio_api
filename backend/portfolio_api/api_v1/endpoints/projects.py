from typing import List
from fastapi import APIRouter
from portfolio_api.data.json import JsonDataService
from portfolio_api.models import Project

router = APIRouter()


@router.get("/", response_model=List[Project])
def read_projects():
    return JsonDataService.Projects()
