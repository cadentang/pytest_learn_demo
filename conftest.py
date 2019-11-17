# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
"""
# import pytest
#
# def pytest_addoption(parser):
#     parser.addoption("--cmdopt", action="store", default="type1",
#         help="my option: type1 or type2")
#
# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")
#
# @pytest.fixture
# def aa():
#     return pytest.config.getoption("--cmdopt")

import os
import pytest
import allure
from selenium import webdriver

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


@allure.step("打开浏览器")
def fixture_step():
    pass

@pytest.fixture
def init_url():
    fixture_step()
    yield True


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            dirpng = r'./base/output/'
            if os.path.exists(dirpng) and os.path.isdir(dirpng):
                pass
            else:
                os.mkdir(dirpng)

            file_name = dirpng + report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            _capture_screenshot(file_name)
            with open(file_name, mode='rb') as f:
                file = f.read()
            allure.attach(file, "错误截图", allure.attachment_type.PNG)


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# pytest自定义命令参数,env:执行的环境，project：项目名称，port:端、移动端或者PC端
def pytest_addoption(parser):
    parser.addoption("--env")
    parser.addoption("--project")
    parser.addoption("--port")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def project(request):
    return request.config.getoption("--project")

@pytest.fixture
def port(request):
    return request.config.getoption("--port")

@pytest.fixture(scope='session', autouse=True)
def browser():
    # print(env)
    global driver, env
    # print(env)
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope='session', autouse=True)
def get_env():
    global env

    return env
