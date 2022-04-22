from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


#rota que responde com a página


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html",{"request":request})