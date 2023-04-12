# s='  hello!'
# print(s.split(" "))
# print(type)
import os

# for word in "Python":
#     if (word == 'o'):
#         break
#     print(word, end="  ")
#
# for word in "Python":
#     if (word == 'o'):
#         continue
# print(word, end="  "
# path=os.getcwd()
# print(path)
# path1=os.path.realpath(__file__)
# print(path1)
# path2=os.getcwd()+"/python"
# print(path2)
# os.mkdir(path2)
# path3=os.path.join(os.getcwd(),"tets/oo")
# print(path3)
# os.mkdir(path3)
# print(os.path.isfile(__file__))
# print(os.path.isdir(os.getcwd()))
# print(os.path.exists("D:\project\lianxi\main1.py"))
# print(os.listdir(os.getcwd()))

# def digui():
# for path in os.listdir(os.getcwd()):
#     if os.path.isdir(path):
#         os.listdir(os.path.join(os.getcwd(),path))
#     else:
#          print(os.path.join(os.getcwd(),path))
# try :
#     os.rmdir("oo")
# except  Exception as e:
#     print("错误{0}".format(e))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
#     # print("*"*i)
# ----*
# ---***
# --*****
# -*******
# ********

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(" * ", end="")
    print("")

for i in  range(1,10):#1 2
    for j in range(1, i+1):#1 2
        print("{0} * {1}={2}".format(i,j,i*j ),end="  ")
    print("")

