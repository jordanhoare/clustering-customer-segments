import uvicorn
from app.app import app
from app.config import settings


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app, host=settings.host, port=settings.port, log_level=settings.log_level
    )


if __name__ == "__main__":
    run()
