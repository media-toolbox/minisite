from typing import Callable

from fastapi import FastAPI


def preload_something():
    """
    In order to load something on the memory of each worker.
    """
    pass


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        preload_something()

    return start_app
