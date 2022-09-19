from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "ChangelogRest"

    API_STR: str = "/api"

    PORT_API_URL: str = "https://api.getport.io/v1"
    PORT_CLIENT_ID: str = 'YOUR_CLIENT_ID'
    PORT_CLIENT_SECRET: str = 'YOUR_CLIENT_SECRET'
    SLACK_WEBHOOK_URL: str = "YOUR_WEBHOOK_URL"

    class Config:
        case_sensitive = True


settings = Settings()
