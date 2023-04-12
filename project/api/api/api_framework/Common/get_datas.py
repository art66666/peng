import requests
from api.api_framework.Common.project_path import *
from api.api_framework.Common.base_page import BasePage


class GetData:
    # 获取会话session
    @staticmethod
    def get_session():
        session = requests.session()
        return session

    header = {"Authorization": "Basic aW9tczppb21z"}

    headers = {"Authorization": BasePage(access_token_path).read_yaml()["access_token"],"Content-Type":"application/json"}

    upload_headers = {"Authorization": BasePage(access_token_path).read_yaml()["access_token"]}