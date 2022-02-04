from fastapi import FastAPI
from fastapi.params import Body
from psycopg import Cursor
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time 

app = FastAPI()

class Post(BaseModel):
    title: str
    contents: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database='fastapi', user='postgres'
        ,password='Haleem001', cursor_factory=RealDictCursor)
        cursor= conn.cursor
        print("Database connection was successful")
        break
    except Exception as error:
        print("connection to database failed")
        print ("Error", error)
        time.sleep(3)

#my_post=[{b}]
#@app.get("/")
#def root():
    #return {"message": "Hello World"}



@app.get('/posts/')
def get_posts():
    return{'data':'This is your posts'}



@app.post('/createpost/')
def create_post(new_post:Post):
    print(new_post)
    return{'data:new post'}
    