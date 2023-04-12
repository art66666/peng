# Select类-下拉框操作
# selenium提供了Select类来处理select/option
#
# 引入类：
from selenium.webdriver.support.ui import Select
# 启动谷歌浏览器
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service_log_path="E:\\chromedrive_service.log")
#全局等待 隐性等待
# driver.implicitly_wait(30)
# 访问一个网址
driver.get("http://www.baidu.com")
driver.maximize_window()
#1、先找到鼠标要操作的元素
ele=driver.find_element(By.XPATH,'//*[@id="u1"]//*[@name="tj_settingicon"]')
# ele.click()
# #2、实例化ActionChains类
# ac=ActionChains(driver)
#
# # 3、将鼠标操作添加到actions列表中
# ac.move_to_element(ele)
#
# #4、调用perform()来执行鼠标操作
# ac.perform()

# 让下拉列表显示出来
ActionChains(driver).move_to_element(ele).perform()

# 选择下拉列表当中的 高级搜索
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//*[text()="高级搜索"]')))
driver.find_element(By.XPATH,'//*[text()="高级搜索"]').click()

# 选择下拉列表值:
# 1、通过下标选择：select_by_index(index)从0开始；
# 2、通过value属性：select_by_value(value值)
# 3、通过文本内容：select_by_visible_text(文本内容)
# ele=driver.find_element(By.XPATH,'//*[@id="u1"]//*[@name="tj_settingicon"]')
# ele.click()
# 1、找到select元素
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[text()="所有网页和文件"]')))
select_ele=driver.find_element(By.XPATH,'//div[text()="所有网页和文件"]')
# 实例化Select类
s=Select(select_ele)
#3、选择下拉列表值
#方式一：下标从0开始
s.select_by_index(1)
# 方式二： value值
s.select_by_value("stf=1647931018.701,1679467018.701|stftype=1")
# 方式三：文本内容
s.select_by_visible_text("一月内")