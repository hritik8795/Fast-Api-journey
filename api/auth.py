from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.database import get_db
from models.user import User
from schemas.user import  UserCreate
from core.security import hash_password, verify_password, create_access_token   

router =APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register")
async def register(user:UserCreate,db:AsyncSession=Depends(get_db)):
    db_user = User(username=user.username,email=user.email,password=hash_password(user.password))
    db.add(db_user)
    await db.commit()
    return {"message":"User created successfully"}



from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }