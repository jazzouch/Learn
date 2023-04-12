import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 测试类
class TestLagou():
    # 在用例执行之前的操作
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # 在用例执行之后的操作
    def teardown_method(self, method):
        self.driver.quit()

    def test_Lagou(self):
        # 打开一个网页
        self.driver.get("https://www.lagou.com/")
        # 等待弹出框
        time.sleep(2)
        # 点击弹出框的X
        self.driver.find_element(By.ID, "cboxClose").click()
        time.sleep(1)
        # 定位搜索框并输入
        self.driver.find_element(By.ID, "search_input").send_keys("高级测试工程师")
        # 定位搜索按钮并点击
        self.driver.find_element(By.ID, "search_button").click()
        time.sleep(20)









