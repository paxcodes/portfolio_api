from typing import List

from fastapi import APIRouter
from portfolio_api.data import JsonDataService
from portfolio_api.models import FeaturedPR, OtherPR

router = APIRouter()


@router.get("/featured", response_model=List[FeaturedPR])
def read_featured_pull_requests():
    return JsonDataService.FeaturedPullRequests()


@router.get("/other", response_model=List[OtherPR])
def read_other_pull_requests():
    return JsonDataService.OtherPullRequests()
