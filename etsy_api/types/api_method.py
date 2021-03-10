import urllib
import httpx
from ..exceptions import MethodVisibilityException, UnknownApiException, BadRequestException, ForbiddenException
from ..exceptions import NotFoundException, ServerSideException, ServiceUnavailableException
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
        
        if r.status_code not in [200, 201]:
            exception_details = r.headers.get('X-Error-Detail')
            exception_class = UnknownApiException
            if r.status_code == 400:
                exception_class = BadRequestException
            elif r.status_code == 403:
                exception_class = ForbiddenException
            elif r.status_code == 404:
                exception_class = NotFoundException
            elif r.status_code == 500:
                exception_class = ServerSideException
            elif r.status_code == 503:
                exception_class = ServiceUnavailableException
            
            raise exception_class(f'Got {r.status_code}. Error details: {exception_details}')
        
        return r.json()
