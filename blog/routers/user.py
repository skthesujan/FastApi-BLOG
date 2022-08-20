from fastapi import APIRouter,Depends,status,HTTPException
import database,schemas,models,hashing
from sqlalchemy.orm import Session
from repository import user


router=APIRouter(
    prefix='/user',
    tags=['USERS']
)
get_db=database.get_db

@router.post('/',response_model=schemas.showUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)



@router.get('/{id}',response_model=schemas.showUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.get_user(id,db)
