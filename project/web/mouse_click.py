# 鼠标操作
# 由selenium的ActionChains类来完成模拟鼠标操作。
# 主要操作流程：
# 1、存储鼠标操作
# 2、perform()来执行操作
#
# 支持的操作如下：
# double_click 双击操作
# context_click 右击操作
# drag_and_drop 拖拽操作。左键按住拖动一个元素到另一个区域，然后释放按键
# move_to_element()...鼠标悬停。经常用到
#
# perform()
# 引入ActionChains类：
# from selenium.webdriver.common.action_chains import ActionChains
# AC.方法名1().context_click().perform()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动谷歌浏览器
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
sleep(3)
