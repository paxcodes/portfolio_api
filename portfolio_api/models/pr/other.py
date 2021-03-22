from typing import List

from pydantic import BaseModel

from ..tech import Tech


class OtherPR(BaseModel):
    project: str  # e.g. pytest-dev/pytest
    count: int
    contribIcon: List[Tech]
