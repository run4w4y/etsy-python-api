import urllib
import httpx
from ..exceptions import MethodVisibilityException
from ..api_key import EtsyApiKey
from dataclasses import dataclass


# TODO: [ ] different usage of api_key if oauth is required
@dataclass
class ApiMethod:
    base_url = 'https://openapi.etsy.com/v2'
    name: str=''
    description: str=''
    uri: str='/'
    params: dict=None
    defaults: dict=None
    return_type: str=''
    visibility: str='public'
    http_method: str='GET'
    api_key: EtsyApiKey=None
    
    async def __call__(self, **kwargs):
        timeout = 20
        if kwargs.get('timeout') is not None:
            timeout = kwargs['timeout']
            del kwargs['timeout']
            
        request_args = { 'method': self.http_method, 'api_key': self.api_key.keystring }
        
        request_args.update(kwargs)
        args_encoded = urllib.parse.urlencode(request_args)
        async with httpx.AsyncClient() as client:
            r = await client.get(f'{self.base_url}{self.uri}?{args_encoded}', timeout=timeout)
            r.raise_for_status() # TODO: [ ] should handle it in a better way
        
        return r.json()
