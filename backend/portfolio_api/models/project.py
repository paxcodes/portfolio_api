from typing import Dict, List, Optional
from urllib.parse import urlparse

from pydantic import BaseModel, validator

from .tech import Tech


class Screenshot(BaseModel):
    src: str
    alt: str


class Project(BaseModel):
    title: str
    builtWith: List[Tech]
    description: str
    screenshots: List[Screenshot]
    github: Optional[List[str]]  # ['paxcodes/dicery_backend', 'paxcodes/dicery_app']
    link: Optional[str]

    @validator("screenshots", pre=True)
    def cast_to_screenshot_model(cls, value: List[Dict[str, str]]) -> List[Screenshot]:
        return [Screenshot(**screenshot) for screenshot in value]

    @validator("link", pre=True)
    def validate_link(cls, value: Optional[str]) -> Optional[str]:
        if isinstance(value, str):
            parsed_link = urlparse(value)
            if None in [parsed_link.scheme, parsed_link.netloc, parsed_link.path]:
                raise ValueError(value)
            return value
        if value is not None:
            raise ValueError(value)
        return value
