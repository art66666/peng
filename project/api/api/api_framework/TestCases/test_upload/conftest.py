import pytest
from Common.cnn_db import Db_util

@pytest.fixture(scope="class")
def check_sql():
    print("****查询sql的前置****")
    yield
    print("****查询SQL的后置***")
    after_sql = Db_util().selecttest("secect * from i_point_info where i_point_name = '3'")
    return after_sql[""]