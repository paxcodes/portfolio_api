import json
from pathlib import Path
from typing import List

from portfolio_api.models import FeaturedPR, OtherPR, Project

JSON_FILE_DIR = Path(__file__).parent / "json_files"


class JsonDataService:
    @staticmethod
    def FeaturedPullRequests() -> List[FeaturedPR]:
        with open(Path(JSON_FILE_DIR, "pr_featured.json"), "r") as f:
            data = json.load(f)
        return [FeaturedPR(**pr) for pr in data]

    @staticmethod
    def OtherPullRequests() -> List[OtherPR]:
        with open(Path(JSON_FILE_DIR, "pr_other.json"), "r") as f:
            data = json.load(f)
        return [OtherPR(**pr) for pr in data]

    @staticmethod
    def Projects() -> List[Project]:
        with open(Path(JSON_FILE_DIR, "projects.json"), "r") as f:
            data = json.load(f)
        return [Project(**project) for project in data]
