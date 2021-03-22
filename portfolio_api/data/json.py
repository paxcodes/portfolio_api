import json
from pathlib import Path
from typing import List

from portfolio_api.models.pr.featured import FeaturedPR

JSON_FILE_DIR = Path(__file__).parent / "json_files"


class JsonDataService:
    @staticmethod
    def FeaturedPullRequests() -> List[FeaturedPR]:
        with open(Path(JSON_FILE_DIR, "pr_featured.json"), "r") as f:
            data = json.load(f)
        return [FeaturedPR(**pr) for pr in data]
