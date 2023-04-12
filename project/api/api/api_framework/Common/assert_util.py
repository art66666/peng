"""
断言封装
"""
from api.api_framework.Common.my_log import MyLog
import json


class AssertUtil:

    @staticmethod
    def assert_code(code,excepted_code):
        """'
        断言判断code值是否相等
        """
        try:
            assert int(code) == int(excepted_code)
            MyLog().info('返回值"{0}"与数据断言"{1}"一致，断言通过'.format(code,excepted_code))
            return True
        except:
            MyLog().error("code错误，code是{0}，except_code是{1}".format(code,excepted_code))
            raise

    @staticmethod
    def assert_status_code(res_status_code,except_status_code):
        """
        判断响应的状态值是否相等
        """
        try:
            assert int(res_status_code) == int(except_status_code)
            MyLog().info('返回状态值值"{0}"与数据断言"{1}"一致，断言通过'.format(res_status_code,except_status_code))
            return True
        except:
            MyLog().error('状态值错误，请求返回的状态值为"{0}"，断言状态值为"{1}"'.format(res_status_code,except_status_code))
            raise

    @staticmethod
    def assert_body(body,except_body):
        """
        判断返回结果内容是否相等
        """
        try:
            assert body == except_body
            MyLog().info('返回数据"{0}"与数据断言"{1}"一致，断言通过'.format(body,except_body))
            return True
        except:
            MyLog().error('返回结果错误，请求返回的结果内容为"{0}"，断言的内容为"{1}"'.format(body,except_body))
            raise

    @staticmethod
    def assert_in_body(body,except_body):
        """
        验证返回结果是否包含期望内容
        """
        try:
            body = json.dumps(body)
            assert except_body in body
            MyLog().info('数据断言"{0}"在返回数据"{1}"内，断言通过'.format(body,except_body))
            return True
        except:
            MyLog().error('返回结果不包含断言内容，请求返回的结果内容为"{0}"，断言的内容为"{1}"'.format(body,except_body))
            raise