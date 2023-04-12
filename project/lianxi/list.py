# 在列表末尾添加新的对象
list = ['Google', 'baidu', 'T']
list.append('taobao')
print(list)

# 将指定对象插入列表
list = ['Google', 'baidu', 'T', 'baidu']
list.insert(1, "Nick")
print(list)

# 在列表末尾追加另一个序列中的多个值
list = ['Google', 'baidu', 'T', 'baidu']
list2 = ['nick', 'baidu']
list.extend(list2)
print(list)

# 统计某个元素在列表中出现的次数
list = ['Google', 'baidu', 'T', 'baidu']
a = list.count('baidu')
print(a)

# 从列表中找出某个值第一个匹配项的索引位置
list = ['Google', 'baidu', 'T', 'baidu']
a = list.index('baidu')
print(a)

# 移除列表中的一个元素（默认最后一个元素）
list = ['Google', 'baidu', 'T', 'baidu']
list.pop()
print(list)

# 移除列表中某个值的第一个匹配项
list = ['Google', 'baidu', 'T', 'baidu']
list.remove('baidu')
print(list)

# 清空列表
list = ['Google', 'baidu', 'T']
list.clear()
print(list)

# 删除指定索引位置
list = ['Google', 'baidu', 'T', 'baidu']
del list[2]
print(list)

list = ['Google', 'baidu', 'T', 'baidu']
# del list[1:3] #-->顾头不顾尾
# print(list)
del list[0:2]
print(list)
# 复制列表
list = ['Google', 'baidu', 'T']
list2 = list.copy()
print(list2)

# 对原列表进行排序
list = ['Google', 'baidu', 'T', 'baidu']
list.sort()#降序排列
print(list)

# 反向列表中元素
list = ['Google', 'baidu', 'T', 'baidu']
list.reverse()
print(list)