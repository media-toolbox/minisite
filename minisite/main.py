import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy.util import asbool

from .api.content import router as api_router
from .core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION, config
from .core.events import create_start_app_handler


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()

if asbool(config.get("MS_WP_AUTH")):
    app.add_middleware(DBSessionMiddleware, db_url=config.get("MS_WP_DATABASE_URI"))


def run():
    uvicorn.run(
        "minisite.main:app", host="0.0.0.0", port=8092, reload=True, debug=False
    )


if __name__ == "__main__":
    run()
