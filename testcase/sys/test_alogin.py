from common.commonData import CommonData
from conftest import http
import pytest
import allure

@allure.feature("登录模块")
@pytest.mark.alogin
class Test_class:
    path = '/sys/login'
    #验证登录成功
    def test_login_success(self):
        data={"userName":CommonData.mobile,"password":CommonData.pwd}
        repo_login=http.post(self.path,data)
        assert repo_login['code']==200
        assert repo_login['msg']=='操作成功'
        assert repo_login['object']['userId']==113
    #验证用户不存在
    @allure.story('校验登录失败')
    def test_login_failed(self):
        data = {"userName": "1"+CommonData.mobile, "password": CommonData.pwd}
        repo_login=http.post(self.path,data)
        assert repo_login['code']==301
        assert repo_login['msg']=='用户不存在'
    #验证密码错误
    @allure.story('校验密码错误')
    def test_error_pwd(self):
        data = {"userName": CommonData.mobile, "password": CommonData.pwd+'123'}
        repo_login=http.post(self.path,data)
        assert repo_login['code']==410
        assert repo_login['msg']=='用户名或密码错误'
    #验证用户为“”
    @allure.story('校验用户为空')
    def test_null_user(self):
        data={"userName":"","password":CommonData.pwd}
        repo_login=http.post(self.path,data)
        assert repo_login['code']==3010
        assert repo_login['msg']=='此账户禁止登录'
    #验证无userName参数
    @allure.story('校验无用名参数')
    def test_none_user(self):
        data = {"password": CommonData.pwd}
        repo_login = http.post(self.path, data)
        assert repo_login['code']==301
        assert repo_login['msg']=='用户不存在'



