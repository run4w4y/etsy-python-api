from ..types import ApiMethod, Listing
from ..types.string_enum import StringEnum
from enum import auto
from typing import Optional, Sequence
import json


class SortOn(StringEnum):
    CREATED = auto()
    PRICE = auto()
    SCORE = auto()


class SortOrder(StringEnum):
    UP = auto()
    DOWN = auto()


class GeoLevel(StringEnum):
    CITY = auto()
    STATE = auto()
    COUNTRY = auto()


class find_all_listing_active(ApiMethod):
    def __init__(self, api_key=None):
        super().__init__(
            uri = '/listings/active',
            name='getMethodTable',
            return_type='ApiMethod',
            api_key = api_key
        )

    async def __call__(
        self, 
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        page: Optional[int] = None,
        keywords: Optional[str] = None,
        sort_on: Optional[SortOn] = None,
        sort_order: Optional[SortOrder] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        color: Optional[str] = None, # TODO: [ ] change type to color_triplet later
        color_accuracy = None, # TODO: [ ] change type to color_wiggle
        tags: Optional[Sequence[str]] = None,
        taxonomy_id: Optional[int] = None,
        location: Optional[str] = None,
        lat: Optional[float] = None, # TODO: [ ] change type to latitude
        lon: Optional[float] = None, # TODO: [ ] change type to longtitude
        region: Optional[str] = None, # TODO: [ ] change type to region
        geo_level: Optional[GeoLevel] = None,
        accepts_gift_cards: Optional[bool] = None,
        translate_keywords: Optional[bool] = None
    ):
        kwargs = {}

        for arg_key, arg_value in locals().items():
            if arg_value is not None and arg_key not in ['__class__', 'self', 'kwargs']:
                kwargs[arg_key] = arg_value

        res = await super().__call__(**kwargs)
        
        # TODO: [+] add json processing here
        with open('res.json', 'w') as f:
            f.write(json.dumps(res, indent=4))
        
        new_res = (res['count'], list(map(lambda x: Listing.deserialize_with_enums(x), res['results'])))
        print(new_res)
        return new_res