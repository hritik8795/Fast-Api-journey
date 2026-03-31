from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# DATABASE_URL = "postgresql://postgres:yourpassword@localhost/yourdb"
# DATABASE_URL = "postgresql://postgres:12345@localhost/fastapicrud"
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
