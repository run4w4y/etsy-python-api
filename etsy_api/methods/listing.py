from ..types import ApiMethod, Listing
from ..types.string_enum import StringEnum
from .. import types
from enum import auto
from typing import Optional, Sequence
from .paginated_result import PaginatedResult
from .pagination import Pagination
import json
import inspect

def _association_lookup(name: str):
    members = dict(inspect.getmembers(types))
    return members.get(name)


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
        translate_keywords: Optional[bool] = None,
        includes: Optional[str] = None, # specify an association TODO: do a better job with associations
        timeout: Optional[int] = 20 # timeout for request in seconds
    ):
        kwargs = {}

        for arg_key, arg_value in locals().items():
            if arg_value is not None and arg_key not in ['__class__', 'self', 'kwargs']:
                kwargs[arg_key] = arg_value

        res = await super().__call__(**kwargs)

        new_res = []
        for json_listing in res['results']:
            if includes is not None:
                for association in map(lambda x: x.strip(), includes.split(',')):
                    json_listing[association.lower()] = _association_lookup(association)(**json_listing[association])
                    del json_listing[association]
            
            new_res.append(Listing(**json_listing))
        
        return PaginatedResult(total_count=res['count'], results=new_res, pagination=Pagination(**res['pagination']))