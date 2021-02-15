from ..types import ApiMethod


# TODO: [ ] complete
class get_method_table(ApiMethod):
    def __init__(self, api_key=None):
        super().__init__(
            uri = '/',
            name='getMethodTable',
            return_type='ApiMethod',
            api_key = api_key
        )

    async def __call__(self):
        res = await super().__call__(self)
        print(res)
        return res