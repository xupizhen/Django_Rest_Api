class CommonException(Exception):
    """公共异常类"""

    def __init__(self, enum_cls):
        self.code = enum_cls.code
        self.message = enum_cls.message
        self.enum_cls = enum_cls
        super().__init__()


class BusinessException(CommonException):
    """业务异常类"""
    pass


class APIException(CommonException):
    """接口异常类"""
    pass
