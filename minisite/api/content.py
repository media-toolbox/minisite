import pkg_resources
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from minisite.core import config

router = APIRouter()

# Configure template loader with multiple directories.
template_directory = pkg_resources.resource_filename("minisite", "templates")
template_directories = [template_directory]
MS_TEMPLATE_FOLDER = config.config.get("MS_TEMPLATE_FOLDER", default=None)
if MS_TEMPLATE_FOLDER is not None:
    template_directories.insert(0, MS_TEMPLATE_FOLDER)
templates = Jinja2Templates(directory=template_directories)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    tplvars = {
        "request": request,
        "content_template": "content.html",
        "id": id,
        "config": config.all(),
    }
    return templates.TemplateResponse("index.html", context=tplvars)
