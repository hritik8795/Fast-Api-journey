# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# import os

# DATABASE_URL ="postgresql+asyncpg://postgres:12345@localhost:5432/BlogApp"
# engine = create_async_engine(DATABASE_URL,echo=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
# Base = declarative_base()

# async def get_db():
#     async with SessionLocal() as session:
#         yield session


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text
import asyncio
import os

DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/blogapp"

engine = create_async_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session

# ✅ New function to check DB connection
async def check_db_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database is connected successfully!")
    except Exception as e:
        print("❌ Database connection failed:", str(e))

# ✅ Run check (for testing / startup)
if __name__ == "__main__":
    asyncio.run(check_db_connection())