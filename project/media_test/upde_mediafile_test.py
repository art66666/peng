import requests
from requests.auth import HTTPBasicAuth
url_add='https://svr-6-9010.share.51env.net/api/v1/media'
# 定义接口参数
# datainfo={"username":"xuezhangmen","password":"bwf51"}
# response=requests.post(url,data=datainfo).json()
# 定义新增的媒体文件的数据字典
file={
        "media_file":open(r'C:\Users\mi\Desktop\国际稳定版测试工具\测试文档.txt','rb'),
        "filename":"测试文档.txt",
        "Content-Disposition":"form-data",
        "Content-Type":"application/octet-stream"
}
# 定义auth认证
# 发送接口请求并获取返回结果
response=requests.post(url_add,files=file,auth=HTTPBasicAuth("xuezhangmen","bwf51")).json()
print(response["friendly_token"])
friendly_token=response["friendly_token"]
url_updata="https://svr-6-9010.share.51env.net/api/v1/media/"+str(friendly_token)
# 定义接口参数
media_data={"description":"genxin1"}
reponse=requests.put(url_updata,data=media_data,auth=HTTPBasicAuth("xuezhangmen","bwf51")).json()
print(reponse)






