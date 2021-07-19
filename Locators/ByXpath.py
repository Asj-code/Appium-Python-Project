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

# xpath + content description
ele_xpath = driver.find_element_by_xpath("//android.widget.Button[@content-desc='Btn1']").click()

# xpath + resource id
# ele_resource_id = driver.find_element_by_xpath("//android.widget.Button['com.code2lead.kwad:id/EnterValue']").click()

# xpath + index value
# ele_resource_id = driver.find_element_by_xpath("//android.widget.Button[1]").click()

# xpath + text
# ele_xpath = driver.find_element_by_xpath("//android.widget.Button[@text='ScrollView']").click()

# xpath + className
ele_xpath = driver.find_element_by_xpath('//android.widget.EditText').send_keys("hola")

