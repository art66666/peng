user_info = {
    "name": "nick",
    "age": 18,
    "job": "pythoner"
}

# 根据key获取值
a = user_info.get("age")
print(a)
a = user_info.get("Age", 19
)
print(a)

# 所有的key 列表
a = user_info.keys()
print(a)

# 所有的值，values
a = user_info.values()
print(a)

# 所有项的列表形式
a = user_info.items()
print(a)

# 获取并在字典中移除
user_info.pop('age')
print(user_info)

# 随机并在字典中移除
user_info.popitem()
user_info.popitem()
print(user_info)

# 清除内容
a = user_info.clear()
print(a)

# 浅拷贝
a = user_info.copy()
print(a)

# 如果key不存在，则创建，如果存在，则返回已存在的值且不修改
a = user_info.setdefault("age")
print(a)
user_info.setdefault("cool")
print(user_info)

# 从序列键和值设置为value来创建一个新的字典
a = dict.fromkeys(user_info)
print(("new dict: %s") % str(a))

# 更新（两个字典）
user_info = {
    "name": "nick",
    "age": 18,
    "job": "pythoner"
}
user_info2 = {
    "wage": 800000000,
    "drem": "The knife girl"
}
user_info.update(user_info2)
print(user_info)

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')