class Teacher:
    name="花花"
    age="13"
    def coding(self):#实例方法
        print(self.name+"会敲代码")
    @classmethod#类方法
    def swimming(cls):
        print("会游泳")
    @staticmethod
    def sing():
        print("会唱歌")

t=Teacher() #隐式传递
t.coding()
Teacher.coding(t)#显示传递
t.swimming()
Teacher.swimming()
t.sing()
Teacher.sing()
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

n = int(input('请输入等边三角形的行数：'))

for i in range(n):
    # 输出空格
    for j in range(n-i-1):
        print(' ', end='')
    # 输出星号
    for k in range(2*i+1):
        print('*', end='')
    # 换行
    print()
