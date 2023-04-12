import pytest
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.base_page import BasePage
from api.api_framework.Common.project_path import *
from api.api_framework.TestDatas import common_data as CD
from api.api_framework.ApiPath.apiurl import ApiUrl
from api.api_framework.Common.get_datas import GetData

mylog = MyLog()


@pytest.fixture(scope="class")
def login_api():
    mylog.info("*******测试接口前登陆操作*********")
    mylog.info("*******接口请求")
    res = GetData.get_session().request('get', url=ApiUrl.login_url, params=CD.data, headers=GetData.header)
    access_token = 'Bearer ' + res.json()["access_token"]
    mylog.info("******存储access_token*******{0}".format(access_token))
    BasePage(access_token_path).write_yaml({"access_token":access_token})
    yield
    mylog.info("******接口测试结束******")
