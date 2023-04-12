import pytest
from api.api_framework.Common.get_datas import GetData
from api.api_framework.ApiPath.apiurl import ApiUrl
from api.api_framework.Common.base_page import BasePage
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.project_path import *
from api.api_framework.Common.assert_util import AssertUtil
from api.api_framework.Common.cnn_db import Db_util
import allure


@allure.feature("删除点位接口")
@pytest.mark.usefixtures("login_api")
class TestDeletePoint:
    @pytest.mark.parametrize("delete",BasePage(delete_point_path).read_yaml())
    @pytest.mark.smoke
    def test_delete_point(self,delete):
        allure.dynamic.title("删除点位成功")
        url = ApiUrl.batch_dalete_point_url
        method = 'delete'
        data = delete["data"]
        data_ids = delete["data"]["ids"]
        before_sql = Db_util().selecttest("select * from i_point_info where id = {0}".format(data_ids))
        MyLog().info("删除接口操作前id为'{0}'的删除状态为'{1}'".format(data_ids,before_sql[0]["delete_flag"]))
        res = GetData.get_session().request(method,url=url,params=data,headers=GetData.headers)
        AssertUtil.assert_body(res.json()["msg"],"操作成功")
        after_sql = Db_util().selecttest("select * from i_point_info where id = {0}".format(data_ids))
        AssertUtil.assert_code(after_sql[0]["delete_flag"],1)