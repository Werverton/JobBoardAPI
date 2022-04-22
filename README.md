# JobBoardAPI
An API made with FastAPI and Python to insert jobs search.

To run enter in the backend folder and run:
#First need to install all dependencies running:

pip install -r requirements.txt

#The database is postresql you have to install and setup the archive .env inside the backend folder with the local configurations.

#Finally run:
uvicorn main:app --host "0.0.0.0" --port "8000"
Or
to development tasks:
uvicorn main:app --reload
