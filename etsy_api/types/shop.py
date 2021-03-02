from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Shop:
    shop_id: Optional[int] = None
    shop_name: Optional[str] = None
    user_id: Optional[int] = None
    creation_tsz: Optional[float] = None
    title: Optional[str] = None
    announcement: Optional[str] = None
    currency_code: Optional[str] = None
    is_vacation: Optional[bool] = None
    vacation_message: Optional[str] = None
    sale_message: Optional[str] = None
    digital_sale_message: Optional[str] = None
    last_updated_tsz: Optional[float] = None
    listing_active_count: Optional[int] = None
    digital_listing_count: Optional[int] = None
    login_name: Optional[str] = None
    accepts_custom_requests: Optional[bool] = None
    policy_welcome: Optional[str] = None
    policy_payment: Optional[str] = None
    policy_shipping: Optional[str] = None
    policy_refunds: Optional[str] = None
    policy_additional: Optional[str] = None
    policy_seller_info: Optional[str] = None
    policy_updated_tsz: Optional[float] = None
    policy_has_private_receipt_info: Optional[bool] = None
    vacation_autoreply: Optional[str] = None
    ga_code: Optional[str] = None
    url: Optional[str] = None
    image_url_760x100: Optional[str] = None
    num_favorers: Optional[int] = None
    languages: Optional[List[int]] = None
    upcoming_local_event_id: Optional[int] = None
    icon_url_fullxfull: Optional[str] = None
    is_using_structured_policies: Optional[bool] = None
    has_onboarded_structured_policies: Optional[bool] = None
    has_unstructured_policies: Optional[bool] = None
    policy_privacy: Optional[str] = None 
    use_new_inverntory_endpoints: Optional[bool] = None
    include_dispute_form_link: Optional[bool] = None
    is_direct_checkout_onboarded: Optional[bool] = None # not specified in api specs
    is_calculated_eligible: Optional[bool] = None # not specified in api specs
    is_opted_in_to_buyer_promise: Optional[bool] = None # not specified in api specs
    is_shop_us_based: Optional[bool] = None # not specified in api specs
    custom_shops_state: Optional[int] = None # not specified in api specs
