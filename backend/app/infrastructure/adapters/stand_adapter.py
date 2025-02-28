from typing import List
from app.infrastructure.orm_models.stand_model import Stand as ORMStand, StandPart as ORMStandPart, StandAttributes as ORMStandAttributes
from app.domain.stand_domain import Stand as DomainStand, StandPart as DomainStandPart, StandAttributes as DomainStandAttributes
from app.schemas.stand_schema import StandSchema, StandPartSchema, StandAttributesSchema

# --------- ORM Model to Domain Model Adapters ---------


def orm_to_domain(orm_stand: ORMStand) -> DomainStand:
    """
    Convert an ORM Stand object to a Domain Stand object.
    """
    return DomainStand(
        stand_oid=orm_stand.stand_oid,
        od_object_type=orm_stand.od_object_type,
        stand_parts=[orm_to_domain_stand_part(part) for part in orm_stand.stand_part_children],
    )


def orm_to_domain_stand_part(orm_stand_part: ORMStandPart) -> DomainStandPart:
    """
    Convert an ORM StandPart object to a Domain StandPart object.
    """
    return DomainStandPart(
        stand_part_oid=orm_stand_part.stand_part_oid,
        stand_oid=orm_stand_part.stand_oid,
        stand_pnt_part_oid=orm_stand_part.stand_pnt_part_oid,
        od_part_type=orm_stand_part.od_part_type,
        rte_scenario_oid=orm_stand_part.rte_scenario_oid,
        effective_date=orm_stand_part.effective_date,
        expiry_date=orm_stand_part.expiry_date,
        stand_attributes=[orm_to_domain_stand_attributes(attr) for attr in orm_stand_part.stand_attribute_children],
    )


def orm_to_domain_stand_attributes(orm_attr: ORMStandAttributes) -> DomainStandAttributes:
    """
    Convert an ORM StandAttributes object to a Domain StandAttributes object.
    """
    return DomainStandAttributes(
        stand_part_oid=orm_attr.stand_part_oid,
        effective_date=orm_attr.effective_date,
        relate=orm_attr.relate,
        stand_number=orm_attr.stand_number,
        status=orm_attr.status,
        timber_type=orm_attr.timber_type,
        harvest_code=orm_attr.harvest_code,
        established_year=orm_attr.established_year,
        last_thinned_date=orm_attr.last_thinned_date,
        last_thinned_year=orm_attr.last_thinned_year,
        first_thin_year=orm_attr.first_thin_year,
        second_thin_year=orm_attr.second_thin_year,
        third_thin_year=orm_attr.third_thin_year,
        site_index=orm_attr.site_index,
        source=orm_attr.source,
        old_id_1=orm_attr.old_id_1,
        old_id_2=orm_attr.old_id_2,
        ownership=orm_attr.ownership,
        description=orm_attr.description,
        species=orm_attr.species,
        co_dom_species=orm_attr.co_dom_species,
        regeneration_type=orm_attr.regeneration_type,
        special_area_flag=orm_attr.special_area_flag,
        survival_status=orm_attr.survival_status,
        survival_checked=orm_attr.survival_checked,
        strata=orm_attr.strata,
        reserved_timber_stand_flag=orm_attr.reserved_timber_stand_flag,
        sold_flag=orm_attr.sold_flag,
        old_oid=orm_attr.old_oid,
        gng_idx_import_flag=orm_attr.gng_idx_import_flag,
        decremented_from_ss_flag=orm_attr.decremented_from_ss_flag,
        slope=orm_attr.slope,
        aspect=orm_attr.aspect,
        elevation=orm_attr.elevation,
        edx_in_progress_flag=orm_attr.edx_in_progress_flag,
    )


# --------- Domain Model to Pydantic Schema Adapters ---------


def domain_to_schema_stand(domain_stand: DomainStand) -> StandSchema:
    """
    Convert a Domain Stand object to a Pydantic StandSchema.
    """
    return StandSchema(
        stand_oid=domain_stand.stand_oid,
        od_object_type=domain_stand.od_object_type,
        stand_parts=[domain_to_schema_stand_part(part) for part in domain_stand.stand_parts],
    )


def domain_to_schema_stand_part(domain_stand_part: DomainStandPart) -> StandPartSchema:
    """
    Convert a Domain StandPart object to a Pydantic StandPartSchema.
    """
    return StandPartSchema(
        stand_oid=domain_stand_part.stand_oid,
        stand_part_oid=domain_stand_part.stand_part_oid,
        stand_pnt_part_oid=domain_stand_part.stand_pnt_part_oid,
        od_part_type=domain_stand_part.od_part_type,
        rte_scenario_oid=domain_stand_part.rte_scenario_oid,
        effective_date=domain_stand_part.effective_date,
        expiry_date=domain_stand_part.expiry_date,
        stand_attributes=[domain_to_schema_stand_attributes(attr) for attr in domain_stand_part.stand_attributes],
    )


def domain_to_schema_stand_attributes(domain_attr: DomainStandAttributes) -> StandAttributesSchema:
    """
    Convert a Domain StandAttributes object to a Pydantic StandAttributesSchema.
    """
    return StandAttributesSchema(
        stand_part_oid=domain_attr.stand_part_oid,
        effective_date=domain_attr.effective_date,
        relate=domain_attr.relate,
        stand_number=domain_attr.stand_number,
        status=domain_attr.status,
        timber_type=domain_attr.timber_type,
        harvest_code=domain_attr.harvest_code,
        established_year=domain_attr.established_year,
        last_thinned_date=domain_attr.last_thinned_date,
        last_thinned_year=domain_attr.last_thinned_year,
        first_thin_year=domain_attr.first_thin_year,
        second_thin_year=domain_attr.second_thin_year,
        third_thin_year=domain_attr.third_thin_year,
        site_index=domain_attr.site_index,
        source=domain_attr.source,
        old_id_1=domain_attr.old_id_1,
        old_id_2=domain_attr.old_id_2,
        ownership=domain_attr.ownership,
        description=domain_attr.description,
        species=domain_attr.species,
        co_dom_species=domain_attr.co_dom_species,
        regeneration_type=domain_attr.regeneration_type,
        special_area_flag=domain_attr.special_area_flag,
        survival_status=domain_attr.survival_status,
        survival_checked=domain_attr.survival_checked,
        strata=domain_attr.strata,
        reserved_timber_stand_flag=domain_attr.reserved_timber_stand_flag,
        sold_flag=domain_attr.sold_flag,
        old_oid=domain_attr.old_oid,
        gng_idx_import_flag=domain_attr.gng_idx_import_flag,
        decremented_from_ss_flag=domain_attr.decremented_from_ss_flag,
        slope=domain_attr.slope,
        aspect=domain_attr.aspect,
        elevation=domain_attr.elevation,
        edx_in_progress_flag=domain_attr.edx_in_progress_flag,
    )


# --------- Pydantic Schema to Domain Model Adapters ---------


def schema_to_domain_stand(stand_schema: StandSchema) -> DomainStand:
    """
    Convert a Pydantic StandSchema to a Domain Stand.
    """
    return DomainStand(
        stand_oid=stand_schema.stand_oid,
        od_object_type=stand_schema.od_object_type,
        stand_parts=[schema_to_domain_stand_part(part) for part in stand_schema.stand_parts],
    )


def schema_to_domain_stand_part(stand_part_schema: StandPartSchema) -> DomainStandPart:
    """
    Convert a Pydantic StandPartSchema to a Domain StandPart.
    """
    return DomainStandPart(
        stand_part_oid=stand_part_schema.stand_part_oid,
        stand_oid=stand_part_schema.stand_oid,
        stand_pnt_part_oid=stand_part_schema.stand_pnt_part_oid,
        od_part_type=stand_part_schema.od_part_type,
        rte_scenario_oid=stand_part_schema.rte_scenario_oid,
        effective_date=stand_part_schema.effective_date,
        expiry_date=stand_part_schema.expiry_date,
        stand_attributes=[schema_to_domain_stand_attributes(attr) for attr in stand_part_schema.stand_attributes],
    )


def schema_to_domain_stand_attributes(stand_attr_schema: StandAttributesSchema) -> DomainStandAttributes:
    """
    Convert a Pydantic StandAttributesSchema to a Domain StandAttributes.
    """
    return DomainStandAttributes(
        stand_part_oid=stand_attr_schema.stand_part_oid,
        effective_date=stand_attr_schema.effective_date,
        relate=stand_attr_schema.relate,
        stand_number=stand_attr_schema.stand_number,
        status=stand_attr_schema.status,
        timber_type=stand_attr_schema.timber_type,
        harvest_code=stand_attr_schema.harvest_code,
        established_year=stand_attr_schema.established_year,
        last_thinned_date=stand_attr_schema.last_thinned_date,
        last_thinned_year=stand_attr_schema.last_thinned_year,
        first_thin_year=stand_attr_schema.first_thin_year,
        second_thin_year=stand_attr_schema.second_thin_year,
        third_thin_year=stand_attr_schema.third_thin_year,
        site_index=stand_attr_schema.site_index,
        source=stand_attr_schema.source,
        old_id_1=stand_attr_schema.old_id_1,
        old_id_2=stand_attr_schema.old_id_2,
        ownership=stand_attr_schema.ownership,
        description=stand_attr_schema.description,
        species=stand_attr_schema.species,
        co_dom_species=stand_attr_schema.co_dom_species,
        regeneration_type=stand_attr_schema.regeneration_type,
        special_area_flag=stand_attr_schema.special_area_flag,
        survival_status=stand_attr_schema.survival_status,
        survival_checked=stand_attr_schema.survival_checked,
        strata=stand_attr_schema.strata,
        reserved_timber_stand_flag=stand_attr_schema.reserved_timber_stand_flag,
        sold_flag=stand_attr_schema.sold_flag,
        old_oid=stand_attr_schema.old_oid,
        gng_idx_import_flag=stand_attr_schema.gng_idx_import_flag,
        decremented_from_ss_flag=stand_attr_schema.decremented_from_ss_flag,
        slope=stand_attr_schema.slope,
        aspect=stand_attr_schema.aspect,
        elevation=stand_attr_schema.elevation,
        edx_in_progress_flag=stand_attr_schema.edx_in_progress_flag,
    )


# --------- Domain Model to ORM Adapters ---------


def domain_to_orm(domain_stand: DomainStand) -> ORMStand:
    """
    Convert a Domain Stand to an ORM Stand.
    """
    orm_stand = ORMStand(
        stand_oid=domain_stand.stand_oid,
        od_object_type=domain_stand.od_object_type,
    )
    orm_stand.stand_part_children = [domain_to_orm_stand_part(part) for part in domain_stand.stand_parts]
    return orm_stand


def domain_to_orm_stand_part(domain_stand_part: DomainStandPart) -> ORMStandPart:
    """
    Convert a Domain StandPart to an ORM StandPart.
    """
    orm_stand_part = ORMStandPart(
        stand_part_oid=domain_stand_part.stand_part_oid,
        stand_oid=domain_stand_part.stand_oid,
        stand_pnt_part_oid=domain_stand_part.stand_pnt_part_oid,
        od_part_type=domain_stand_part.od_part_type,
        rte_scenario_oid=domain_stand_part.rte_scenario_oid,
        effective_date=domain_stand_part.effective_date,
        expiry_date=domain_stand_part.expiry_date,
    )
    orm_stand_part.stand_attribute_children = [domain_to_orm_stand_attributes(attr) for attr in domain_stand_part.stand_attributes]
    return orm_stand_part


def domain_to_orm_stand_attributes(domain_attr: DomainStandAttributes) -> ORMStandAttributes:
    """
    Convert a Domain StandAttributes to an ORM StandAttributes.
    """
    return ORMStandAttributes(
        stand_part_oid=domain_attr.stand_part_oid,
        effective_date=domain_attr.effective_date,
        relate=domain_attr.relate,
        stand_number=domain_attr.stand_number,
        status=domain_attr.status,
        timber_type=domain_attr.timber_type,
        harvest_code=domain_attr.harvest_code,
        established_year=domain_attr.established_year,
        last_thinned_date=domain_attr.last_thinned_date,
        last_thinned_year=domain_attr.last_thinned_year,
        first_thin_year=domain_attr.first_thin_year,
        second_thin_year=domain_attr.second_thin_year,
        third_thin_year=domain_attr.third_thin_year,
        site_index=domain_attr.site_index,
        source=domain_attr.source,
        old_id_1=domain_attr.old_id_1,
        old_id_2=domain_attr.old_id_2,
        ownership=domain_attr.ownership,
        description=domain_attr.description,
        species=domain_attr.species,
        co_dom_species=domain_attr.co_dom_species,
        regeneration_type=domain_attr.regeneration_type,
        special_area_flag=domain_attr.special_area_flag,
        survival_status=domain_attr.survival_status,
        survival_checked=domain_attr.survival_checked,
        strata=domain_attr.strata,
        reserved_timber_stand_flag=domain_attr.reserved_timber_stand_flag,
        sold_flag=domain_attr.sold_flag,
        old_oid=domain_attr.old_oid,
        gng_idx_import_flag=domain_attr.gng_idx_import_flag,
        decremented_from_ss_flag=domain_attr.decremented_from_ss_flag,
        slope=domain_attr.slope,
        aspect=domain_attr.aspect,
        elevation=domain_attr.elevation,
        edx_in_progress_flag=domain_attr.edx_in_progress_flag,
    )
