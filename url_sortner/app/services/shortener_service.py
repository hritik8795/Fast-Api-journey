from sqlalchemy.orm import Session
from app.repositories.url_repo import( create_short_url,get_by_short_code)
from app.utils.generator import generate_short_code


def create_url_service(db:Session,original_url:str):
    short_code = generate_short_code()
    return create_short_url(db,original_url,short_code) 

def get_original_url_services(db:Session,short_code:str):
    return get_by_short_code(db,short_code)