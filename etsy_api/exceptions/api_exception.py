class ApiException(Exception):
    pass

class MethodVisibilityException(ApiException):
    pass

# status code 400
class BadRequestException(ApiException):
    pass

# status code 403
class ForbiddenException(ApiException):
    pass

# status code 404
class NotFoundException(ApiException):
    pass

# status code 500
class ServerSideException(ApiException):
    pass

# status code 503
class ServiceUnavailableException(ApiException):
    pass

# neither of the status codes above
class UnknownApiException(ApiException):
    pass
