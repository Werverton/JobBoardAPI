from fastapi import FastAPI
from core.config import settings
#from apis.general_pages.route_homepage import general_pages_router
from fastapi.staticfiles import StaticFiles
from db.session import engine
from db.base import Base
from apis.base import api_router


#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)



def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_table():
    print("create_tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_table()
    return app

app = start_application()