import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException


desire_caps = {}
desire_caps['platformName'] = 'Android'
desire_caps['platformVersion'] = '8.1.0'
desire_caps['deviceName'] = 'generic_x86'
desire_caps['automationName'] = 'UiAutomator1'
desire_caps['appPackage'] = 'com.code2lead.kwad'
desire_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desire_caps['app'] = ('/Users/avalith/Desktop/Android_Demo_App.apk')


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)

wait = WebDriverWait(driver, 30, poll_frequency= 1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

long_press_ele = driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))')

action = TouchAction(driver)
action.long_press(long_press_ele, 5)
action.perform()

time.sleep(2)
driver.quit()