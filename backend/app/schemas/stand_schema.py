# Pydantic Models (AKA Schemas)

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class StandAttributesSchema(BaseModel):
    stand_part_oid: str
    effective_date: Optional[datetime] = None
    relate: Optional[str] = None
    stand_number: Optional[str] = None
    status: Optional[str] = None
    timber_type: Optional[str] = None
    harvest_code: Optional[str] = None
    established_year: Optional[str] = None
    last_thinned_date: Optional[datetime] = None
    last_thinned_year: Optional[str] = None
    first_thin_year: Optional[str] = None
    second_thin_year: Optional[str] = None
    third_thin_year: Optional[str] = None
    site_index: Optional[int] = None
    source: Optional[str] = None
    old_id_1: Optional[str] = None
    old_id_2: Optional[str] = None
    ownership: Optional[str] = None
    description: Optional[str] = None
    species: Optional[str] = None
    co_dom_species: Optional[str] = None
    regeneration_type: Optional[str] = None
    special_area_flag: Optional[str] = None
    survival_status: Optional[str] = None
    survival_checked: Optional[datetime] = None
    strata: Optional[str] = None
    reserved_timber_stand_flag: Optional[str] = None
    sold_flag: Optional[str] = None
    old_oid: Optional[str] = None
    gng_idx_import_flag: Optional[str] = None
    decremented_from_ss_flag: Optional[str] = None
    slope: Optional[float] = None
    aspect: Optional[float] = None
    elevation: Optional[float] = None
    edx_in_progress_flag: Optional[str] = None


class StandPartSchema(BaseModel):
    stand_oid: str
    stand_part_oid: str
    stand_pnt_part_oid: Optional[str] = None
    od_part_type: str
    rte_scenario_oid: Optional[str] = None
    effective_date: datetime
    expiry_date: Optional[datetime] = None
    # The relationship from SQLAlchemy's 'stand_attribute_children'
    stand_attributes: List[StandAttributesSchema] = []


class StandSchema(BaseModel):
    stand_oid: str
    od_object_type: str
    # You can map SQLAlchemy's 'stand_part_children' to this field.
    stand_parts: List[StandPartSchema] = []
