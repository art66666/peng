import requests
url="https://svr-6-9010.share.51env.net/api/v1/login"
datainfo={"username":"xuezhangmen","password":"bwf51"}
response=requests.post(url,data=datainfo).json()
print(response)
result=response['username']
print(result)
exresult=datainfo['username']
if result==exresult:
    print("接口成功")
else:
    print("接口失败")
