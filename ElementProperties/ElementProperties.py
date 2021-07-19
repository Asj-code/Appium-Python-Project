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


ele_id = driver.find_element_by_id('com.code2lead.kwad:id/EnterValue')
print("Is displayed: ", ele_id.is_displayed())
print("Is enabled: ", ele_id.is_enabled())
print("Is selected: ", ele_id.is_selected())
print("Size: ", ele_id.size)
print("Location: ", ele_id.location)
