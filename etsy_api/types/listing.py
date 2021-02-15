from .featured_rank import featured_rank
from .who_made import WhoMade
from .weight_unit import WeightUnit
from .dimensions_unit import DimensionsUnit
from .recipient import Recipient
from .occasion import Occasion
from .auto_deserialize import AutoDeserialize
from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass
class Listing(AutoDeserialize):
    listing_id: Optional[int] = None
    state: Optional[str] = None
    user_id: Optional[int] = None
    category_id: Optional[int] = None # deprecated
    title: Optional[str] = None
    description: Optional[str] = None
    creation_tsz: Optional[float] = None
    ending_tsz: Optional[float] = None
    original_creation_tsz: Optional[float] = None
    last_modified_tsz: Optional[float] = None
    price: Optional[str] = None
    currency_code: Optional[str] = None
    quantity: Optional[int] = None
    sku: Optional[Sequence[str]] = None
    tags: Optional[Sequence[str]] = None
    taxonomy_id: Optional[int] = None
    suggested_taxonomy_id: Optional[int] = None
    taxonomy_path: Optional[Sequence[str]] = None
    materials: Optional[Sequence[str]] = None
    shop_section_id: Optional[int] = None
    featured_rank: Optional[featured_rank] = None
    state_tsz: Optional[float] = None
    url: Optional[str] = None
    views: Optional[int] = None
    num_favorers: Optional[int] = None
    shipping_template_id: Optional[int] = None
    shipping_profile_id: Optional[int] = None # deprecated
    processing_min: Optional[int] = None
    processing_max: Optional[int] = None
    who_made: Optional[WhoMade] = None
    is_supply: Optional[bool] = None
    when_made: Optional[str] = None
    item_weight: Optional[int] = None
    item_weight_unit: Optional[WeightUnit] = None
    item_length: Optional[int] = None
    item_width: Optional[int] = None
    item_height: Optional[int] = None
    item_dimensions_unit: Optional[DimensionsUnit] = None
    is_private: Optional[bool] = None
    recipient: Optional[Recipient] = None
    occasion: Optional[Occasion] = None
    style: Sequence[str] = None
    non_taxable: Optional[bool] = None
    is_customizable: Optional[bool] = None
    is_digital: Optional[bool] = None
    file_data: Optional[str] = None
    can_write_inventory: Optional[bool] = None # supposedly private
    has_variations: Optional[bool] = None
    should_auto_renew: Optional[bool] = None
    language: Optional[str] = None
    is_vintage: Optional[bool] = None # not listed in the API specs
    used_manufacturer: Optional[bool] = None # not listed in the API specs
