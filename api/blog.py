from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_current_user
from db.database import get_db
from models.blog import Blog
from schemas.blog import BlogCreate
from core.deps import get_current_user

router =APIRouter(prefix="/blogs",tags=["blogs"])

@router.post("/")
async def create_blog(blog:BlogCreate,db:AsyncSession=Depends(get_db),user=Depends(get_current_user)):
    new_blog =Blog(**blog.dict(),owner_id=user.id)
    db.add(new_blog)
    await db.commit()
    return {"message":"blog created successfully"}

@router.get("/")
async def get_blogs(skip:int=0,limit:int=10,db:AsyncSession=Depends(get_db)):
    result =await db.execute(select(Blog).where(Blog.is_published==True).offset(skip).limit(limit))
    return result.scalars().all()

@router.put("/{blog_id }")
async def update_blog(blog_id:int,blog:BlogCreate,db:AsyncSession=Depends(get_db), user=Depends(get_current_user)):
    result =await db.execute(select(Blog).where(Blog.id==blog_id))
    db_blog =result.scalar_one_or_none()
    if not db_blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    if db_blog.owner_id !=user.id:
        raise HTTPException(status_code=403,detail="Not authorized to update this blog")
    for key,value in blog.dict().items():
        setattr(db_blog,key,value)
    await db.commit()
    return {"message":"Blog updated successfully"}  

@router.delete("/{blog_id}")
async def delete_blog(blog_id:int,db:AsyncSession=Depends(get_db),user=Depends(get_current_user)):
    result =await db.execute(select(Blog).where(Blog.id==blog_id))
    db_blog =result.scalar_one_or_none()

    if not db_blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    if db_blog.owner_id !=user.id:
        raise HTTPException(status_code=403,detail="Not authorized to delete this blog")
    await db.delete(db_blog)
    await db.commit()
    return {"message":"Blog deleted successfully"}  