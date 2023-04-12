import allure
from Common.get_datas import GetData
from Common.my_log import MyLog
from ApiPath.apiurl import ApiUrl
from Common.assert_util import AssertUtil
import pytest

mylog = MyLog()


@pytest.mark.usefixtures("login_api")
@allure.feature("获取菜单接口")
class TestMenu:
    def test_menu(self):
        mylog.info("*********菜单接口开始测试*******")
        mylog.info("*********获取url********")
        url = ApiUrl.menu_url
        mylog.info("********获取请求头access_token*******")
        headers = GetData.headers
        mylog.info("*******菜单接口请求********")
        res = GetData.get_session().request('get', url=url, headers=headers)
        AssertUtil.assert_body(res.json()["msg"],"success")
        mylog.info("*********菜单接口测试结束*******")
