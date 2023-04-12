# data = [10, 4, 33, 21, 54, 8, 11, 5, 22, 2, 17, 13, 3, 6, 1, ]
#
# print("before sort:", data)
#
# for j in range(1, len(data)):
#     for i in range(len(data) - j):
#         if data[i] > data[i + 1]:
#             temp = data[i]
#             data[i] = data[i + 1]
#             data[i + 1] = temp
#     print(data)
#
# print("after sort:", data)

# import re
#
# s = 'nick jenny nice'
#
# # 匹配方式（一）
# b = re.match(r'nick', s)
# q = b.group()
# print(q)

# import sys
# for i in sys.path:
#     print(i)
# import sys
# import os
# pre_path = os.path.abspath('../')
# sys.path.append(pre_path)

import time
print(time.time())
print(time.ctime())