from ..types import ApiMethod
from typing import Optional


# TODO: [ ] complete
class get_method_table(ApiMethod):
    def __init__(self, api_key=None):
        super().__init__(
            uri = '/',
            name='getMethodTable',
            return_type='ApiMethod',
            api_key = api_key
        )

    async def __call__(self, timeout: Optional[int] = 20):
        res = await super().__call__(timeout=timeout)
        print(res)
        return res
    