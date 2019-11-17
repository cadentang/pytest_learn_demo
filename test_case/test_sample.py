# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
"""
from selenium import webdriver
import pytest
import allure

# @allure.step("打开浏览器")
# def get_browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver

@allure.step("打开网页")
def open_url(driver, url):
    driver.get(url)

@allure.step("搜索框中输入文字")
def search(driver, locator, text):
    driver.find_element_by_xpath(locator).send_keys(text)

class TestSearch:

    def test_search(self, browser, get_env):
        print(get_env)
        url = "http://www.baidu.com"
        search_locator = '//*[@id="kw"]'
        search_button = '//*[@id="su"]'
        search_text = "python"
        open_url(browser, url)
        search(browser, search_locator, search_text)
        with allure.step("点击搜索按钮"):
            browser.find_element_by_xpath(search_button).click()

        # with allure.step('添加失败截图...'):
        #     allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

        assert browser.title == search_text + "_百度搜索"


