from typing import List, Union
from urllib.parse import ParseResult, urlparse

from pydantic import BaseModel, validator

from ..tech import Tech


class FeaturedPR(BaseModel):
    project: str  # e.g. pytest-dev/pytest
    issueNum: int
    link: ParseResult
    title: str
    contribIcon: List[Tech]

    @validator("link", pre=True)
    def parse_link(cls, value: Union[ParseResult, str]) -> ParseResult:
        if isinstance(value, str):
            return urlparse(value)
        elif isinstance(value, ParseResult):
            return value
        raise ValueError(value)
