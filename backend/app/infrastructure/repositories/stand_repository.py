from app.infrastructure.orm_models.stand_model import Stand as ORMStand
from app.domain.stand_domain import Stand as DomainStand
from app.infrastructure.adapters import stand_adapter
from sqlalchemy.orm import Session
from typing import Optional


def get_stand(db_session: Session, stand_oid: str) -> Optional[DomainStand]:
    orm_stand: Optional[ORMStand] = db_session.query(ORMStand).filter(ORMStand.stand_oid == stand_oid).first()
    if orm_stand is None:
        return None
    return stand_adapter.orm_to_domain_stand_part(orm_stand)
