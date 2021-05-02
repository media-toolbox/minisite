import pkg_resources
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from minisite.core import config

router = APIRouter()

template_directory = pkg_resources.resource_filename("minisite", "templates")
templates = Jinja2Templates(directory=template_directory)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", context={"request": request, "id": id, "config": config.all()}
    )
