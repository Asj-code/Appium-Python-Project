from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pytest

desire_caps = {}
desire_caps['platformName'] = 'Android'
desire_caps['platformVersion'] = '8.1.0'
desire_caps['deviceName'] = 'generic_x86'
desire_caps['automationName'] = 'UiAutomator1'
desire_caps['appPackage'] = 'com.builtwithscience'
desire_caps['appActivity'] = 'com.builtwithscience.MainActivity'
# desire_caps['app'] = ('/Users/avalith/Desktop/Android_Demo_App.apk')


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)


wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

ele = wait.until(lambda x: x.driver.find_elements_by_class_name('android.view.ViewGroup'))
# def test_verify_login():
#     try:
#         element = driver.find_elements_by_class_name('android.view.ViewGroup')
#         error = WebDriverWait(driver, 30).until(EC.presence_of_element_located(element))
#         for x in element:
#             login = x.text
#             if login == 'Login':
#                 x.click()
#     except:
#         print("Login successfully")

# by xpath
# ele_xpath = driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()
# '//android.widget.TextView[@test="Login"]'