from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.PageLocators.loginpage_loacators import LoginPageLocator as loc
from selenium import webdriver
from selenium.webdriver.common.by import By
#点击 用户名密码方式
# driver.find_element(By.ID,'TANGRAM__PSP_11__changePwdCodeItem').click()
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    # 登录操作
    def login(self,username,password,remeber_user=True):
        # 输入用户名
        # 输入密码
        # 点击登录
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//*[@name="emp_DomainName"]')))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(password)
        #判断一下rember_user的值，来决定是否勾选。
        self.driver.find_element(*loc.login_but).click()
        # 判断处理
    # 注册入口
    # def register(self):
    #     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '')))
    #     self.driver.find_element(By.XPATH,'').click()
    #
    # 获取错误提示信息 -登录区域
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="Submit"]//span[@class="help-block"]')))
        return self.driver.find_element(By.XPATH,'//div[@id="Submit"]//span[@class="help-block"]').text
#
#     # 获取错误信息 页面正中间
#     # def get_errorMsg_from_pageCenter(self):
#     #     pass
#     # 忘记密码
