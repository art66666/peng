from selenium.webdriver.common.by import By
class LoginPageLocator:
    name_text = (By.XPATH,'//*[@name="emp_DomainName"]')
    pwd_text = (By.XPATH,'//*[@name="emp_Password"]')
    login_but = (By.XPATH,'//input[@id="BtnLogin"]')
    errorMsg_from_loginArea=(By.XPATH, '//span[@class="help-block"]')
