import os

from pydantic import BaseModel


class Server(BaseModel):
    port: str
    host: str


class Endpoint(BaseModel):
    url: str


class AppConfig(BaseModel):
    server: Server
    endpoint: Endpoint


def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    endpoint = os.environ['ENDPOINT']

    return AppConfig(
        server=Server(port=app_port, host=app_host),
        endpoint=Endpoint(url=endpoint),
    )


config = load_from_env()
