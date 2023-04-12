# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print("{0} is eating...{1}".format(self.name, food))
#
#
# d = Dog("shabi")
# choice = input(">>>:").strip()
#
# print(hasattr(d, choice))

class Foo:
    f = '类的静态变量'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hi(self):
        print('hi,%s'%self.name)

obj=Foo('egon',73)

#检测是否含有某属性
print(hasattr(obj,'name'))   #True
print(hasattr(obj,'say_hi'))  #True

#获取属性
n=getattr(obj,'name')
print(n)    #egon
func=getattr(obj,'say_hi')
func()     # hi,egon

# print(getattr(obj,'aaaaaaaa','不存在啊')) #报错

#设置属性
setattr(obj,'sb',True)
setattr(obj,'show_name',lambda self:self.name+'sb')
print(obj.__dict__)   #{'name': 'egon', 'age': 73, 'sb': True, 'show_name': <function <lambda> at 0x0097C5D0>}
print(obj.show_name(obj))   #egonsb
#用setattr为对象设置方法时：需要在（）内手动传入绑定的对象，不能直接obj.show_name()，会报错

#删除属性
delattr(obj,'age')
delattr(obj,'show_name')
# delattr(obj,'show_name111')#不存在,则报错

print(obj.__dict__)   #{'name': 'egon', 'sb': True}

# class A(object):
#     def __init__(self):
#         self.name = 'python'
#         self.age = 18
#
#     def func(self):
#         return self.age
#
# obj1 = A()
#
# #检查对象是否含有成员
# print(hasattr(obj1,'age')) #True
# print(hasattr(obj1,'func')) #True
#
# #获取对象成员
# print(getattr(obj1,'name')) #python
# print(getattr(obj1,'func'))  #<bound method A.func of <__main__.A object at 0x000000C0C7B9D048>>
#
# #设置对象成员
# setattr(obj1,'slary',9999)
# print(getattr(obj1,'slary')) #9999
#
# #删除成员
# delattr(obj1,'slary')
# print(hasattr(obj1,'slary')) #False
class Page:

    name = "hello"
    des = "hello world"
    btn = "btn"

    def click(self):
        print("click button")

    def clear(self):
        print("clear")

    def fill(self, text):
        print(f"input text: {text}")


if __name__ == '__main__':
    p = Page()
    print(p.name)
    print(p.click())
    p = Page()
    # 获取对象属性
    name = getattr(p, "name")
    print(name)
    # 调用对象方法
    getattr(p, "click")()
    # # 方法带参数
    getattr(p, "fill")("yo yo")
p = Page()
# 先判断后调用
if hasattr(p, "click"):
    getattr(p, "click")()
delattr(p, "click")
print(p.click)
setattr(p, 'age', 22)
print(getattr(p, 'age'))
