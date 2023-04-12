import pytest
from api.api_framework.Common.get_datas import GetData
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.base_page import BasePage
from api.api_framework.ApiPath.apiurl import ApiUrl
from api.api_framework.Common.project_path import *
from api.api_framework.Common.assert_util import AssertUtil as AU
import allure

mylog = MyLog()


# 整个接口描述
@allure.feature("登录接口")
class TestLogin:
    # 登录接口
    @pytest.mark.parametrize('args', BasePage(login_data_path).read_yaml())
    # 用例优先级    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, args):
        mylog.info("*********登录接口开始测试*******")
        mylog.info(args)
        url = ApiUrl.login_url
        method = args["requests"]["method"]
        data = args["requests"]["data"]
        headers = args["requests"]["headers"]
        res = GetData.get_session().request(method, url, params=data, headers=headers)
        name = args["name"]
        allure.dynamic.title(name)  # 展示每条用例的名称
        allure.dynamic.description("请求body==>> %s" % str(data))  # 展示每天用例的请求体
        try:
            AU.assert_body(res.json()["username"], args["except"]["username"])
        except:
            AU.assert_body(res.json()["msg"],args["except"]["msg"])
        mylog.info("******登录接口测试结束*******")

