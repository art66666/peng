# 元素定位
# id、classname 、tagname、name
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动谷歌浏览器
# driver = webdriver.Chrome(service_log_path="D:\\chromedrive_service.log")
driver = webdriver.Chrome()

# 访问一个网址
driver.get("http://www.baidu.com")

# 方式一 id
# ele=driver.find_element(By.ID, 'kw')
# print(ele)
# print(ele.get_attribute("class"))


# 方式二 class
# ele=driver.find_elements(By.CLASS_NAME,'s_ipt')
# driver.find_element(By.CLASS_NAME,'s_ipt')

# #方式三 name
# driver.find_element(By.NAME,"wd")
# driver.find_elements(By.NAME,"wd")

# #方式四 tagname
# driver.find_element(By.TAG_NAME,'input')
# driver.find_elements(By.TAG_NAME,'input')

#方式五、六  针对链接
# driver.find_element(By.LINK_TEXT,'新闻')
# driver.find_element(By.PARTIAL_LINK_TEXT,'闻')

#xpath
driver.find_element(By.XPATH,'//*[@id="kw"]')
#绝对定位 以/开头 非常依赖于页面的顺序和位置 父/子
#相对定位 以//开头 不依赖页面的顺序和位置。只看 整个页面当中有没有符合表达式的元素
# //标签名称[@属性值=值]

# 函数使用：
# text():元素的text内容
# 例://*[@id="XXX"]//p[text()="XXX"]
# contains(@属性/text(),value):包含函数。
# 例:contains(@class,"XXX")、contains(text(),"XXX")
# //input[contains(@class,"username")]
# 逻辑运算 and or //标签名称[@属性名称=值 and @属性名称=值]
# 例：//div[@class="XXX"and contains(@style,"display:visibility")]
# 应用场景：
# 一个页面的几个操作，都会有弹出框出现。定位到弹出框会有几个。
# 但通过display的值来定位到当前提示的那一个。

# xpath轴定位
# 轴运算：
# ancestor:祖先节点 包括父
# parent:父节点
# preceding:当前元素节点标签之前的所有结点。(html页面先后顺序)
# preceding-sibling:当前元素节点标签之前的所有兄弟结点
# following；当前元素节点标签之后的所有结点。(html页面先后顺序)
# following-sibing:当前元素节点标签之后的所有兄弟结点
# 实用语法：
# /轴名称::节点名称[@属性=值]
# 例://div//table//td//preceding::td
#
# 较多的应用场景：
# 页面显示为一个表格样式的数据列。需要通过组合来定位元素
#层级定位
#css

sleep(3)
