from time import sleep
from selenium import webdriver

# 启动谷歌浏览器
driver = webdriver.Chrome(service_log_path="E:\\chromedrive_service.log")

# 访问一个网址
driver.get("http://www.baidu.com")

# 结束回话
# driver.quit()

# 窗口最大化
driver.maximize_window()

# 访问
driver.get("http://www.taobao.com")

# 回退到上一页
driver.back()

# 回退到下一页
driver.forward()

# 刷新
driver.refresh()

# 获取标题
print(driver.title)

# 获取网址
print(driver.current_url)

# 窗口的句柄
print(driver.current_window_handle)

sleep(3)
