from fastapi import FastAPI
#from blog import schemas,models
#from blog.database import engine, Base
# from .database import Base
from database import engine
import models
from routers import blog,user,authentication

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

#def get_db():
 #   db=SessionLocal()
  #  try:
   #     yield db
    #finally:
     #   db.close 