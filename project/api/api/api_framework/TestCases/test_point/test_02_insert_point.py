import allure
import pytest
from api.api_framework.ApiPath.apiurl import ApiUrl
from api.api_framework.Common.get_datas import GetData
from api.api_framework.Common.cnn_db import Db_util
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.project_path import *
from api.api_framework.Common.base_page import BasePage
from api.api_framework.Common.assert_util import AssertUtil


@pytest.mark.usefixtures("login_api")
@allure.feature("新增点位接口")
class TestInsertPoint:
    @pytest.mark.parametrize("insert", BasePage(insert_point_path).read_yaml())
    @pytest.mark.smoke
    def test_insert_point(self, insert):
        url = ApiUrl.insert_point_url
        data = insert["data"]
        name = insert["name"]
        method = insert["method"]
        allure.dynamic.title(name)
        allure.dynamic.description("请求body==>> %s" % str(data))
        res = GetData.get_session().request(method, url=url, json=data, headers=GetData.headers)
        try:
            AssertUtil.assert_body(res.json()["msg"], insert["except"]["msg"])
            after_sql = Db_util().selecttest("select * from i_point_info where point_name = '测试数据'")
            MyLog().info(after_sql)
            AssertUtil.assert_body(after_sql[0]['point_name'], insert["data"]["pointName"])
            rep = [{"data":{'ids': after_sql[0]['id']}}]
            BasePage(delete_point_path).write_yaml(rep)
        except:
            AssertUtil.assert_body(res.json()["msg"], "同一个房间中存在名称重复的点位")

