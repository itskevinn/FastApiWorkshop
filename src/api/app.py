from fastapi.applications import FastAPI

from src.api.routers.fibonacci import fibonacci_sequence
from src.api.routers.prime import prime_number


def create_instance() -> FastAPI:
    return FastAPI()


def init_app() -> FastAPI:
    app = FastAPI()
    app.include_router(prime_number.router, prefix="/isPrime")
    app.include_router(fibonacci_sequence.router, prefix="/fibonacci")
    return app


