s = "nick"

# 索引
print(s[0])
print(s[1])
print(s[2])
print(s[3])

# 长度
ret = len(s)
print(ret)

# 切片
print(s[1:3])
print(s.rsplit("ic"))

# 替换
name = "Nick is good, Today is nice day."
a = name.replace("good", "man")
print(a)

# 连接两个字符串
li = ["nick", "serven"]
a = "".join(li)
b = "_".join(li)
print(a)
print(b)

# 指定的分隔符将字符串进行分割
ver="I and Tom and str"
a = ver.rpartition("and")#从右侧分割
print(a)

# 分割，前，中，后三部分
name = "Nick is good, Today is nice day."
a = name.partition("good")#从左侧分割
print(a)

# for循环
for i in s:
    print(i)
for i in range(5):
    print(i)

# 反转
s = 'ssssssssss111'
print(s[::-1])  # 111ssssssssss