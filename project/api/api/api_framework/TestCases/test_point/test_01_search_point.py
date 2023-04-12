import allure
from api.api_framework.Common.get_datas import GetData
from api.api_framework.ApiPath.apiurl import ApiUrl
from api.api_framework.Common.base_page import BasePage
from api.api_framework.Common.project_path import *
from api.api_framework.Common.assert_util import AssertUtil
import pytest
from api.api_framework.Common.cnn_db import Db_util


@pytest.mark.usefixtures("login_api")
@allure.feature("查询点位接口")
class TestPoint:
    @pytest.mark.parametrize('search', BasePage(search_point_path).read_yaml())
    @pytest.mark.smoke
    def test_point(self, search):
        url = ApiUrl.search_point_url
        data = search["data"]
        method = search["method"]
        name = search["name"]
        allure.dynamic.title(name)
        allure.dynamic.description("请求body==>> %s" % str(data))
        res = GetData.get_session().request(method, url=url, params=data, headers=GetData.headers)
        res_count = len(res.json()["data"]["records"])
        after_sql = Db_util().selecttest('select count(1) from i_point_info where room_code = "00101"and delete_flag = 0')
        AssertUtil.assert_body(res_count,after_sql[0]["count(1)"])