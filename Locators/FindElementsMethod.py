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

elements = driver.find_elements_by_class_name("android.widget.Button")

# for element in elements:
#     print(element.text)

for element in elements:
    button = element.text
    if button == "CONTACT US FORM":
        button.click()
        break

