import os

# 项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# test_data路径
test_data_path = os.path.join(project_path, "test_data", "test_data.xlsx")
# test_result路径
test_result_path = os.path.join(project_path, "TestResult", "allure_html", "")
# 配置文件路径
case_config_path = os.path.join(project_path, "Conf", "case.config")
# 配置日志路径
my_log_path = os.path.join(project_path, "TestResult", "log", "test.log")
# allure报告
allure_report = os.path.join(project_path, "TestResult", "report")
# access_token文件路径
access_token_path = os.path.join(project_path, "extract.yaml")
# login接口数据
login_data_path = os.path.join(project_path, "TestDatas", "login_data.yaml")
# upload 接口数据
upload_data_path = os.path.join(project_path, "TestDatas", "upload_data.yaml")
"""
点位接口数据
"""
# 查询点位接口数据
search_point_path = os.path.join(project_path, "TestDatas", "point_datas", "search_point_data.yaml")
# 新增点位接口数据
insert_point_path = os.path.join(project_path, "TestDatas", "point_datas", "insert_point_data.yaml")
# 删除点位接口数据
delete_point_path = os.path.join(project_path, "TestDatas", "point_datas", "delete_point_data.yaml")

"""
设备接口数据
"""
# 新增设备接口数据
insert_device_path = os.path.join(project_path,"TestDatas","device_datas","insert_device_datas.yaml")
