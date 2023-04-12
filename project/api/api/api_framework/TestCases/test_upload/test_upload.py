import allure
from Common.get_datas import GetData
from ApiPath.apiurl import ApiUrl
from Common.my_log import MyLog
from Common.base_page import BasePage
from Common.project_path import *
import pytest

mylog = MyLog()


@pytest.mark.usefixtures("login_api")
@pytest.mark.parametrize('upload', BasePage(upload_data_path).read_yaml())
@allure.feature("测试上传接口")
class TestUpload:
    def test_file_upload(self, upload):
        mylog.info("******上传接口测试开始*******")
        mylog.info(upload)
        url = ApiUrl.upload_url
        data = upload["request"]["data"]
        name = upload["name"]
        res = GetData.get_session().request('post', url=url, files=data, headers=GetData.upload_headers)
        allure.dynamic.title(name)
        allure.dynamic.description("请求body==>> %s" % str(data))
        assert res.json()["msg"] == upload["except"]["msg"]
        mylog.info('接口返回值"{0}"与数据断言"{1}"相等，断言通过'.format(res.json()["msg"], upload["except"]["msg"]))
        mylog.info("******上传接口测试结束*******")
