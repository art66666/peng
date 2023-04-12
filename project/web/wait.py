# 三种等待
# 1、强制等待
# sleep(秒)
# 2、隐性等待
# implicitly_wait(秒)
# 设置最长等待时间，在这个时间内加载完成，则执行下一步。
# 整个driver的会话周期内，设置一次即可，全局有效
# 3、显性等待
# 明确等到某个条件满足之后，再去执行下一步操作。
# 程序每隔XX秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
# WebDriverWait类：显示等待类。
# WebDriverWait(driver,等待时长，轮循周期).until()until_not()
# expected_conditions模块：提供一系列期望发生的条件。
# presence_of_element_located：元素存在

# visibility_of_element_located：元素可见
# element_to_be_clickable:元素可点击
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动谷歌浏览器
driver = webdriver.Chrome(service_log_path="E:\\chromedrive_service.log")
#全局等待
driver.implicitly_wait(30)
# 访问一个网址
driver.get("http://www.baidu.com")
driver.find_element(By.XPATH,'//*[@id="u1"]//a[@name="tj_login"]').click()

#点击 用户名密码方式
driver.find_element(By.ID,'TANGRAM__PSP_11__changePwdCodeItem').click()
