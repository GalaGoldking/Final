from fastapi import FastAPI, Request
import uvicorn
import crud

api = FastAPI()

@api.get('/api/')
def check():
    return {"Hello": "World"}

@api.get('/showAllUsers')
def show_all():
    allUsers = crud.show_all_users()
    for user in allUsers:
        return {"User": user}

@api.get('/user/{session.uid}')
def show_user(user_id):
    pass