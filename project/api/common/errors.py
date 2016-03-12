
"""
ERROR DEFINITION:

1000-1999 Request Errors
2000-2999 Account Errors
"""


class ApplicationException(Exception):
    """Base error class for application.
       code - A numeric code identifying the error for external use
       internal_code - A numeric code identifying the error for internal use
       message - A human-friendly description of the error suitable to display to users."""

    def __init__(self, code, status_code, msg):
        self.code = code
        self.msg = msg
        self.status_code = status_code

    def __str__(self):
        return "[PROFILE-%s] STATUS=%s MESSAGE=%s" % (self.code, self.status_code, self.msg)


class GeneralException(ApplicationException):
    CODE = 1000
    STATUS_CODE = 500
    TEXT = 'General Exception: %s'

    def __init__(self, error='unknown'):
        ApplicationException.__init__(self, self.CODE, self.STATUS_CODE, self.TEXT % error)


class InvalidRequestException(GeneralException):
    CODE = 1001
    STATUS_CODE = 400
    TEXT = 'Invalid request: %s'


class UserInactiveException(GeneralException):
    CODE = 1002
    STATUS_CODE = 403
    TEXT = 'User is not active: %s'


class InvalidAccessTokenException(GeneralException):
    CODE = 1003
    STATUS_CODE = 403
    TEXT = 'Invalid access token: %s'


class InvalidRefreshTokenException(GeneralException):
    CODE = 1004
    STATUS_CODE = 403
    TEXT = 'Invalid refresh token: %s'


class InvalidClientException(GeneralException):
    CODE = 1005
    STATUS_CODE = 403
    TEXT = 'Invalid client: %s'


class InvalidSignatureException(GeneralException):
    CODE = 1006
    STATUS_CODE = 403
    TEXT = 'Invalid signature: %s'


"""
View Based Errors
"""


class InvalidFieldException(GeneralException):
    CODE = 2000
    STATUS_CODE = 400
    TEXT = 'Invalid field: %s'


class InvalidEmailException(GeneralException):
    CODE = 2001
    STATUS_CODE = 400
    TEXT = 'Invalid email: %s'


class EmailConflictException(GeneralException):
    CODE = 2002
    STATUS_CODE = 409
    TEXT = 'Email conflict: %s'


class InvalidCredentialsException(GeneralException):
    CODE = 2003
    STATUS_CODE = 403
    TEXT = 'Invalid credentials: %s'


