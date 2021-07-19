from appium import webdriver


desire_caps = {}
desire_caps['platformName'] = 'IOS'
desire_caps['platformVersion'] = '14.5'
desire_caps['deviceName'] = 'iPhone 11 Pro'
desire_caps['automationName'] = 'XCUITest'
desire_caps['app'] = ('/Users/avalith/Desktop/UICatalog\ copy.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)