
from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database,models,hashing,token1
from sqlalchemy.orm import session
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(
    tags=['AUTHENTICATION']
)
get_db=database.get_db

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    if not hashing.Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password')
    
    
    access_token =token1.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}