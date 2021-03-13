from pydantic import BaseSettings


class Settings(BaseSettings):
    GITHUB_TOKEN: str
    GITHUB_USERNAME: str

    class Config:
        case_sensitive = True


settings = Settings(_env_file=".env", GITHUB_USERNAME="paxcodes")
