from conftest import http
import random
import json
from common.commonData import CommonData
import pytest
import allure

@allure.feature('注册模块')
@pytest.mark.debug
class Test_saveOrUpdateUser:
    weihao = str(random.randint(00000000, 99999999))

    @allure.story('注册用户')
    def test_register(self):
        path='/user/saveOrUpdateUser'
        data={
                "nickName": "ppp",
                "userName": '159'+self.weihao,
                "telNo": "",
                "email": "",
                "address": "",
                "roleIds": "",
                "regionId": 1,
                "regionLevel": 1
              }
        register=http.post(path,data)
        # assert register['code']==500
    #登录
    @allure.story('登录已注册的用户')
    def test_login(self):
        path='/sys/login'
        data={"userName":'159'+self.weihao,"password":CommonData.pwd}
        login=http.post(path,data)
        assert login['code']==200
        return login['object']['userId']

    # 用户列表
    @allure.story('获取用户列表')
    def test_loadUserList(self):
        path='/user/loadUserList'
        data={
            "pageCurrent": 1,
            "pageSize": 10,
            "nickName": "",
            "userName": "",
            "regionId": 1
             }
        repo=http.post(path,data)
        assert  repo['object']['list'][0]['id']==self.test_login()

    #获取用户信息
    @allure.story('获取用户信息')
    def test_loadUserInfo(self):
        path='/user/loadUserInfo'
        data={'id':self.test_login()}
        repo=http.post(path,data)
        assert repo['code']==200
        # js=json.dumps(repo)   #转Json格式
        # print(js)


