from datetime import date
from datetime import datetime
from optparse import Option
from typing import Optional

from pydantic import BaseModel


#shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    company : Optional[str] = None
    company_url : Optional[str] = None
    location : Optional[str] = "Remote"
    description : Optional[str] = None
    date_posted : Optional[str] = datetime.now().date()


#this will be used to validate data while creating a job
class JobCreate(JobBase):
    title :  str
    company : str
    company_url : Optional[str]
    location : Optional[str]
    date_posted : date
    description : Optional[str]

    class Config():#to convert non dict obj to json
        orm_mode= True

class ShowJob(JobBase):
    title : str
    company: str
    company_url : Optional[str]
    location : str
    date_posted : date
    description : Optional[str]

    class Config():  #to convert non dict obj to json
        orm_mode = True
