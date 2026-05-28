from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.shortener_service import create_url_service,get_original_url_services
from app.schemas.url import URLCreate,URLResponse

router = APIRouter()

@router.post("/shorten", response_model=URLResponse)


def create_short_url(payload:URLCreate,db:Session =Depends(get_db)):
    url =create_url_service(db,payload.original_url)
    return {
        "original_url":url.original_url,
        "short_code":url.short_code,
        "short_url":f"http://localhost:8000/{url.short_code}"
    }

@router.get("/{short_code}")
def redirect_url(short_code:str,db:Session=Depends(get_db)):
    url=get_original_url_services(db,short_code)
    if not url:
        raise HTTPException(status_code=404,detail="Url not found")
    return RedirectResponse(url.original_url) 