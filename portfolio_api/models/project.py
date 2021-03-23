from typing import Dict, List, Optional, Union
from urllib.parse import ParseResult, urlparse

from pydantic import BaseModel, validator

from .tech import Tech


class Screenshot(BaseModel):
    src: ParseResult
    alt: str

    @validator("src", pre=True)
    def parse_link(cls, value: Union[ParseResult, str]) -> ParseResult:
        if isinstance(value, str):
            return urlparse(value)
        elif isinstance(value, ParseResult):
            return value
        raise ValueError(value)


class Project(BaseModel):
    title: str
    builtWith: List[Tech]
    description: str
    screenshots: List[Screenshot]
    github: Optional[List[str]]  # ['paxcodes/dicery_backend', 'paxcodes/dicery_app']
    link: Optional[ParseResult]

    @validator("screenshots", pre=True)
    def cast_to_screenshot_model(cls, value: List[Dict[str, str]]) -> List[Screenshot]:
        return [Screenshot(**screenshot) for screenshot in value]

    @validator("link", pre=True)
    def parse_link(cls, value: Optional[str]) -> Optional[ParseResult]:
        if isinstance(value, str):
            return urlparse(value)
        elif isinstance(value, ParseResult) or value is None:
            return value
        raise ValueError(value)
