import pytest
from api.api_framework.Common.get_datas import GetData
from api.api_framework.ApiPath.apiurl import ApiUrl as AU
from api.api_framework.Common.base_page import BasePage
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.project_path import *
import allure
from api.api_framework.Common.cnn_db import Db_util
from api.api_framework.Common.assert_util import AssertUtil


@pytest.mark.usefixtures("login_api")

class TestInsertDevice:
    @pytest.mark.parametrize('insert', BasePage(insert_device_path).read_yaml())
    def test_insert_device(self, insert):
        url = AU.insert_device_url
        data = insert["datas"]
        name = insert["name"]
        method = insert["method"]
        before_sql = insert["check_sql"]["before_sql"]
        after_sql = insert["check_sql"]["after_sql"]
        allure.dynamic.title(name)
        allure.dynamic.description("请求body==>> %s" % str(data))
        if before_sql:
            front_sql = Db_util().selecttest(before_sql)
            MyLog().info("接口请求前数据最大id为{0}".format(front_sql[0]["max(id)"]))
        else:
            MyLog().info("该条用例不需要执行接口前数据校验")
        res = GetData.get_session().request(method, url=url, json=data, headers=GetData.headers)
        AssertUtil.assert_body(res.json()["msg"], insert["except"]["msg"])
        if res.json()["msg"] == "保存成功":
            if after_sql:
                queen_sql = Db_util().selecttest(after_sql)
                MyLog().info("接口请求后数据最大id为{0}".format(queen_sql[0]["max(id)"]))
                if queen_sql[0]["max(id)"] - front_sql[0]["max(id)"] == 1:
                    MyLog().info("数据库数据新增一条")
        else:
            MyLog().info('返回结果提示信息为"{0}"，不需要进行接口数据库校验'.format(res.json()["msg"]))

#
# if __name__ == '__main__':
#     pytest.main(["-vs"])