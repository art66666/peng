import unittest
from selenium import webdriver
from framework.PageObjects.logn_page import LoginPage
from framework.TestDatas import Common_Datas as CD
from framework.PageObjects.index import IndexPage
from framework.TestDatas import  log_datas as LD
import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 通过excel读取本功能当中需要的所有测试数据
        print("========所有测试用例之前的，setup====整个测试类只执行一次=======")
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg = LoginPage(cls.driver)
        pass

    @classmethod
    def tearDownClass(cls):
        print("========所有测试用例之前的，teardown====整个测试类只执行一次=======")
        cls.driver.quit()
        pass

    # def setUp(self):
    #     # 前置 访问登录页面
    #     self.driver=webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.lg=LoginPage(self.driver)
    #     pass

    def tearDown(self):
        # 后置
        self.driver.refresh()
        # self.driver.quit()
        pass

    # 正常用例 -登录成功
    def test_login_1_success(self):
        self.lg.login(LD.success_data["username"],LD.success_data["password"])
        # 前置 访问登录页面
        # 步骤 输入用户名：XXX 密码XXX 点击登录
        # 断言 首页当中-能否找到 退出 这个元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())
        # 等待10秒 元素有没有出现


    # 异常用例 -手机号码格式不对(大于位、小于11位、为空、不在号码段) ddt
    @ddt.data(*LD.phone_data)
    def test_login_0_user_wrongFormat(self,data):
        # 前置 访问登录页面
        # 步骤 输入用户名：XXX 密码XXX 点击登录
        self.lg.login(data["username"],data["password"])
        # 断言 首页当中-能否找到 退出 这个元素
        # 登录页面 获取提示框的文本内容
        # 比对文本内容与期望值 是否相等
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(),data["check"])
    #     pass

    # def test_login_wrongPwd_noReg(self):
    #     # 前置 访问登录页面
    #     # 步骤 输入用户名：XXX 密码XXX 点击登录
    #
    #     # 断言 登录页面 页面正中间提示：XXX
    #     # 登录页面 获取提示框的文本内容
    #     # 比对文本内容与 期望值 是否相等
    #     pass

    # # 异常用例 -用户名为空
    # def test_login_nouser(self):
    #     # 前置 访问登录页面
    #     self.lg.login("", "密码")
    #     # 步骤 输入用户名：XXX 密码XXX 点击登录
    #     # 断言 首页当中-能否找到 退出 这个元素
    #     pass