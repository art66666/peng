import yaml
import subprocess
from api.api_framework.Common.my_log import MyLog
from api.api_framework.Common.project_path import *


mylog = MyLog()

class BasePage:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件
    """
    读取yaml，对yaml反序列化，就是把yaml转换成dict格式
    yaml.load()
    """

    def read_yaml(self):
        with open(self.yaml_file, mode='r', encoding="utf-8") as file:
            value = yaml.load(stream=file, Loader=yaml.FullLoader)
            return value

    # 写入yaml文件
    def write_yaml(self, data):
        with open(self.yaml_file, mode='w', encoding="utf-8") as file:
            value = yaml.dump(data=data, stream=file, allow_unicode=True)



    @staticmethod
    def allure_report(report_path, report_html):
        """
        生成allure报告
        :param report_path:
        :param report_html:
        :return:
        """
        # 执行命令 allure generate
        allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
        mylog.info("报告地址")
        try:
            subprocess.call(allure_cmd, shell=True)
        except:
            mylog.error("执行用例失败，请检查测试环境相关配置")
            raise
