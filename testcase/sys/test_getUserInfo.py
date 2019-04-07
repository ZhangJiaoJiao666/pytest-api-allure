from common.commonData import CommonData
from conftest import http
import pytest
import allure

@allure.feature('获取用户')
@pytest.mark.getUserInfo
class Test_class:

    @allure.story('获取用户成功')
    def test_getUserInfo(self):
        path='/sys/getUserInfo'
        data={"token":CommonData.token}
        repo_getUser=http.post(path,data)
        assert repo_getUser['code']==200
        print("获取用户成功")
