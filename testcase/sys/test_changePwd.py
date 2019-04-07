from conftest import http
from common.commonData import CommonData
import pytest
import allure


@allure.feature('修改密码模块')
class Test_pwd:
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures('recoveyPwd')
    def test_changePwd_success(self):
        newPwd='123456789'
        path='/sys/changePwd'
        data={"userId":162,
              "userName":CommonData.mobile,
              "oldPwd":CommonData.pwd,
              "password":newPwd}
        repo=http.post(path,data)
        assert repo['code']==200
        assert repo['msg']=='操作成功'


    # @pytest.mark.usefixtures('recoveyPwd')
    # def test_oldPwd_error(self):
    #     path='/sys/changePwd'
    #     data={"userId":162,
    #           "userName":CommonData.mobile,
    #           "oldPwd":CommonData.pwd+'1',
    #           'password':'987654'}
    #     repo=http.post(path,data)
    #     assert repo['code']==411
    #     assert repo['msg']=='旧密码错误'

#     @pytest.mark.usefixtures('recoveyPwd')
#     def test_newpwd_null(self):
#         path='/sys/changePwd'
#         data={"userId":162,
#               "userName":CommonData.mobile,
#               "oldPwd":CommonData.pwd,
#               'password':''}
#         repo=http.post(path,data)
#         assert repo['code']==411
#         assert repo['msg']=='旧密码错误'

@pytest.fixture
def recoveyPwd():
    newPwd='123456789'
    yield
    path = '/sys/changePwd'
    data = {"userId": 162,
            "userName": CommonData.mobile,
            "oldPwd": newPwd,
            "password":CommonData.pwd}
    repo = http.post(path, data)
    assert repo['code'] == 200
    assert repo['msg'] == '操作成功'








