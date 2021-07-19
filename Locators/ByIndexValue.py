from appium import webdriver


desire_caps = {}
desire_caps['platformName'] = 'Android'
desire_caps['platformVersion'] = '8.1.0'
desire_caps['deviceName'] = 'generic_x86'
desire_caps['automationName'] = 'UiAutomator1'
desire_caps['appPackage'] = 'com.code2lead.kwad'
desire_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desire_caps['app'] = ('/Users/avalith/Desktop/Android_Demo_App.apk')


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)

ele_index = driver.find_element_by_android_uiautomator("UiSelector().index(4)").click()