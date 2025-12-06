"""Errors"""


class GuwendaoError(BaseException):
    """Base error type for this module"""


class NetworkError(GuwendaoError):
    """A network error has occurred"""


class ParseError(GuwendaoError):
    """A parse error has occurred"""


class UsageError(GuwendaoError):
    """Attempted a usage that is not correct"""
