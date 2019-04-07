import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
    def post(self,path,data):
        proxies = CommonData.proxies        #获取全局变量proxies
        host = CommonData.host
        data_json = json.dumps(data)            #将dict转成json格式
        if CommonData.token is not None:     #判断token是否为空，不为空赋值，为空不加
            self.headers["token"]= CommonData.token
        resp_login = self.http.post(url=host+path,   #发起post请求
                     proxies=proxies,
                     data=data_json,
                     headers=self.headers)
        assert resp_login.status_code == 200   #校验返回码是否为200
        resp_json = resp_login.text             #
        resp_dict = json.loads(resp_json)
        return resp_dict
