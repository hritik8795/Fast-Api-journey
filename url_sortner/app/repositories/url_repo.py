from sqlalchemy.orm import Session
from app.models.url import URL

def create_short_url(db: Session, original_url: str, short_code: str):
    url = URL(original_url=original_url, short_code=short_code)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

def get_by_short_code(db:Session,short_code :str):
    return db.query(URL).filter(URL.short_code == short_code).first()
