from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Pax's Portfolio API"
    API_V1_STR: str = "/v1"
    GITHUB_TOKEN: str
    GITHUB_USERNAME: str

    class Config:
        case_sensitive = True


settings = Settings(_env_file=".env", GITHUB_USERNAME="paxcodes")
