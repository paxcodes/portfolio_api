from typing import List
from urllib.parse import urlparse

from pydantic import BaseModel, validator

from ..tech import Tech


class FeaturedPR(BaseModel):
    project: str  # e.g. pytest-dev/pytest
    issueNum: int
    link: str
    title: str
    contribIcon: List[Tech]

    @validator("link", pre=True)
    def parse_link(cls, value: str) -> str:
        parsed_link = urlparse(value)
        if None in [parsed_link.scheme, parsed_link.netloc, parsed_link.path]:
            raise ValueError(value)
        return value
