# sql alchemy model

from sqlalchemy import (
    CHAR,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Text,
    Numeric,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from ..database import Base


class Stand(Base):
    __tablename__ = "STAND"

    stand_oid: Mapped[str] = mapped_column(String(10), primary_key=True, nullable=False)
    od_object_type: Mapped[str] = mapped_column(CHAR(5), nullable=False)

    # One-to-many relationship: one Stand can have many StandParts
    stand_part_children: Mapped[List["StandPart"]] = relationship()


class StandPart(Base):
    __tablename__ = "STAND_PART"

    stand_oid: Mapped[str] = mapped_column(String(10), ForeignKey("STAND.stand_oid"), nullable=False)
    stand_part_oid: Mapped[str] = mapped_column(String(10), primary_key=True, nullable=False)
    stand_pnt_part_oid: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    od_part_type: Mapped[str] = mapped_column(CHAR(5), nullable=False)
    rte_scenario_oid: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    effective_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    expiry_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)

    # One-to-many relationship: one StandPart can have many StandAttributes
    stand_attribute_children: Mapped[List["StandAttributes"]] = relationship()


class StandAttributes(Base):
    __tablename__ = "STAND_ATTRIBUTES"

    stand_part_oid: Mapped[str] = mapped_column(
        String(10),
        ForeignKey("STAND_PART.stand_part_oid"),
        primary_key=True,
        nullable=False,
    )
    effective_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    relate: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    stand_number: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    status: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    timber_type: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    harvest_code: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    established_year: Mapped[Optional[str]] = mapped_column(String(4), nullable=True)
    last_thinned_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    last_thinned_year: Mapped[Optional[str]] = mapped_column(String(4), nullable=True)
    first_thin_year: Mapped[Optional[str]] = mapped_column(String(4), nullable=True)
    second_thin_year: Mapped[Optional[str]] = mapped_column(String(4), nullable=True)
    third_thin_year: Mapped[Optional[str]] = mapped_column(String(4), nullable=True)
    site_index: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    source: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    old_id_1: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    old_id_2: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    ownership: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    species: Mapped[Optional[str]] = mapped_column(String(25), nullable=True)
    co_dom_species: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    regeneration_type: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    special_area_flag: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    survival_status: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    survival_checked: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
    strata: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    reserved_timber_stand_flag: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    sold_flag: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    old_oid: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    gng_idx_import_flag: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    decremented_from_ss_flag: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    slope: Mapped[Optional[float]] = mapped_column(Numeric(18, 5), nullable=True)
    aspect: Mapped[Optional[float]] = mapped_column(Numeric(18, 5), nullable=True)
    elevation: Mapped[Optional[float]] = mapped_column(Numeric(18, 5), nullable=True)
    edx_in_progress_flag: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
