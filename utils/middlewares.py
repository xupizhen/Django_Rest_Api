import json
import logging

from django.db import DatabaseError
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.http import HttpResponseServerError
from django.middleware.common import MiddlewareMixin

from projectRest import settings
from utils.result import R
from utils.enums import StatusCodeEnum
from utils.exceptions import BusinessException

logger = logging.getLogger(settings.LOGGER_NAME)


class ExceptionMiddleware(MiddlewareMixin):
    """统一异常处理中间件"""

    def process_exception(self, request, exception):
        print('1111')
        """
        统一异常处理
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        if isinstance(exception, BusinessException):
            # 业务异常处理
            data = R.set_result(exception.enum_cls).data()
            return JsonResponse(data)

        elif isinstance(exception, DatabaseError):
            # 数据库异常
            r = R.set_result(StatusCodeEnum.DB_ERR)
            logger.error(r.data(), exc_info=True)
            return JsonResponse(StatusCodeEnum.SERVER_ERR.message)

        elif isinstance(exception, Exception):
            # 服务器异常处理
            r = R.server_error()
            logger.error(r.data(), exc_info=True)
            return JsonResponse(r.data())
        return None
