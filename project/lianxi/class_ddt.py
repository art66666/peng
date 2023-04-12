# import ddt
# import unittest
# Testdata=[{"username":"小明","sex":"男"},
#           {"username":"小红","sex":"女"},
#           {"username":"小花","sex":"女"}]
# @ddt.ddt
# class Test(unittest.TestCase):
#     def setUp(self):
#         print("用例开始执行")
#
#     def tearDown(self):
#         print("用例执行结束")
#
#     @ddt.data(*Testdata)
#     def test_ddt(self,data):
#         print(data)
# if __name__ == '__main__':
#
#     unittest.main()

# class TestClass:
#     def method(self):
#         print("测试方法")
#
# test = TestClass()
# print(TestClass.method) #<unbound method TestClass.method>
# print(test.method) #<bound method TestClass.method of <__main__.TestClass object at 0x021B46D0>>
#
# TestClass.method(test) #测试方法
# test.method() #测试方法

# import yaml
#
# with open('D:\project\lianxi\data\yamlData.yml', 'r', encoding='utf-8') as f:
#     result = yaml.load(f.read(), Loader=yaml.FullLoader)
# print(result, type(result))
# print(result['os'], type(result['os']))
# print(result['osVersion'], type(result['osVersion']))
# print(result['account'], type(result['account']))
# print(result['account']['username'])
# print(result['deviceName'])
# print(result['appPackage'])
# print(result['bool1'], type(result['bool1']))

# import unittest
# import ddt
#
# # 测试数据
# datas = [ {"user": "admin", "psw": "123", "result": "true"},
#         {"user": "admin1", "psw": "1234", "result": "true"},
#         {"user": "admin2", "psw": "1234", "result": "true"},
#         {"user": "admin3", "psw": "1234", "result": "true"},
#         {"user": "admin4", "psw": "1234", "result": "true"},
#         {"user": "admin5", "psw": "1234", "result": "true"},
#         {"user": "admin6", "psw": "1234", "result": "true"},
#         {"user": "admin7", "psw": "1234", "result": "true"},
#         {"user": "admin8", "psw": "1234", "result": "true"},
#         {"user": "admin9", "psw": "1234", "result": "true"},
#         {"user": "admin10", "psw": "1234", "result": "true"},
#         {"user": "admin11", "psw": "1234", "result": "true"}]
#
# @ddt.ddt
# class Test(unittest.TestCase):
#
#     @ddt.data(*datas)
#     def test_(self, d):
#         """上海-悠悠：{0}"""
#         print("测试数据：%s" % d)
#
# if __name__ == "__main__":
#     unittest.main()

import unittest
import ddt

# 测试数据

# datas = [ {"user": "admin", "psw": "123", "result": "true"},
#         {"user": "admin1", "psw": "1234", "result": "true"},
#         {"user": "admin2", "psw": "1234", "result": "true"},
#         {"user": "admin3", "psw": "1234", "result": "true"},
#         {"user": "admin4", "psw": "1234", "result": "true"},
#         {"user": "admin5", "psw": "1234", "result": "true"},
#         {"user": "admin6", "psw": "1234", "result": "true"},
#         {"user": "admin7", "psw": "1234", "result": "true"},
#         {"user": "admin8", "psw": "1234", "result": "true"},
#         {"user": "admin9", "psw": "1234", "result": "true"},
#         {"user": "admin10", "psw": "1234", "result": "true"},
#         {"user": "admin11", "psw": "1234", "result": "true"}]

# datas =[("admin", "123", "true", "用例1描述"),
#         ("admin1", "123", "true", "用例2描述"),
#         ("admin2", "123", "true", "用例3描述"),
#         ("admin3", "123", "true", "用例4描述"),
#         ("admin4", "123", "true", "用例5描述"),
#         ("admin5", "123", "true", "用例6描述"),
#         ]
#
# @ddt.ddt
# class Test(unittest.TestCase):
#
#     @ddt.data(*datas)
#     @ddt.unpack
#     def test_(self, d1, d2, d3, d4):
#         """上海-悠悠：{3}"""
#         print("测试数据：%s" % d1)
#         print("测试数据：%s" % d2)
#         print("测试数据：%s" % d3)
#         print("测试数据：%s" % d4)
#
# if __name__ == "__main__":
#     unittest.main()

name = "Nick is good, Today is nice day."
a = name.replace("good","man")
print(a)

li = ["nick","serven"]
a = "".join(li)
b = "_".join(li)
print(a)
print(b)
s = "nick"
a = s.rpartition(" ")#从右侧分
print(a)

name = "Nick is good, Today is nice day."
a = name.partition("good")#从左侧分
print(a)

s = 'ssssssssss111'
print(s[::-1])  # 111ssssssssss