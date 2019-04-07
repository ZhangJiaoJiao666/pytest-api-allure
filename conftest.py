import pytest
#session/module/class/function
#function对每个函数
# @pytest.fixture(scope='module',autouse=True)  #自动执行（全局初始化操作）
# def module_fixture():
#     print("----公交车到站----")
#     yield
#     print("关门，开车")

# @pytest.fixture(scope='module',autouse=True)
# # def module_fixture():
# #     print("----请投币----")

#
# @pytest.fixture(scope='class',autouse=True)
# def class_fixture():
#     print("--初始化Class-----")
#
# @pytest.fixture(scope='function',autouse=True)  #自动执行（全局初始化操作）
# def function_fixture():
#     print("--初始化Function-----")

import pytest
from common.commonData import CommonData
from util.httpUtil import HttpUtil

http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixtrue():
    path='/sys/login'
    data = {"userName":CommonData.mobile,"password":CommonData.pwd}
    login_respo=http.post(path,data)
    CommonData.token = login_respo['object']['token']   # 获取token
    print("登录成功")
    yield
    path='/sys/logout'
    data=None
    repo=http.post(path,data)
