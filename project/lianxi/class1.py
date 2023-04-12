class Teacher:
    def __init__(self,name,age):#实例方法
        self.name=name
        self.age=age


    def coding(self):#实例方法
        print(self.name+"会敲代码")
    def coking(self,*args):#实例方法
        for item in args:
            print(self.name+"会做{0}".format(item))
    @classmethod#类方法
    def swimming(cls):
        print("会游泳")
    @staticmethod
    def sing():
        print("会唱歌")

# t=Teacher() #隐式传递
# t.coding()
# Teacher.coding(t)#显示传递
# t.swimming()
# Teacher.swimming()
# t.sing()
# Teacher.sing()

#初始化函数
t1=Teacher("小小","15")
# t2=Teacher("意义","18")
# t3=Teacher("积极","16")
# t1.coding()
# t2.coking()
# t3.sing()
t1.coking("炒饭","炒土豆","炒面")