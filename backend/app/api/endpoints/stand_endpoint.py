from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.stand_schema import StandSchema
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.infrastructure.repositories.stand_repository import get_stand
from app.domain.stand_domain import Stand
from app.infrastructure.adapters import stand_adapter


router = APIRouter()


@router.get("/stands/")
async def stands():
    return {"stands": ["9001001001", "9001001002", "9001001098"]}


@router.get("/stands/{stand_oid}/", response_model=StandSchema)
def read_stand(stand_oid: str, db_session: Session = Depends(get_db)):
    domain_stand: Optional[Stand] = get_stand(db_session, stand_oid)
    if domain_stand is None:
        raise HTTPException(status_code=404, detail="Stand not found")
    return stand_adapter.domain_to_schema_stand(domain_stand)
