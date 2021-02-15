import inspect
from . import methods
from .types import ApiMethod
from .api_key import EtsyApiKey


# TODO: [+] try to import all the methods automatically
class EtsyApi:
    def __init__(self, api_key: EtsyApiKey):
        self.api_key = api_key

        for name, obj in inspect.getmembers(methods):
            if inspect.isclass(obj) and issubclass(obj, ApiMethod):
                setattr(self, name, obj(api_key=self.api_key))