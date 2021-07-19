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

print("Check if device is locked or not: ", driver.is_locked())
print("Current package: ", driver.current_package)
print("Current activity: ", driver.current_activity)
print("Current context: ", driver.current_context)
