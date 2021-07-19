from appium import webdriver


desire_caps = {}
desire_caps['platformName'] = 'IOS'
desire_caps['platformVersion'] = '14.5'
desire_caps['deviceName'] = 'iPhone 11 Pro'
desire_caps['automationName'] = 'XCUITest'
desire_caps['app'] = ("/Users/avalith/Library/Developer/Xcode/DerivedData/UICatalog-aztnnokddczsbfbxkmfyuegrdxkx/Build/Products/Debug-iphonesimulator/UICatalog.app")

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)

original_ele = driver.find_element_by_accessibility_id('AAPLActionSheetViewController')
destination_ele = driver.find_element_by_accessibility_id('AAPLTextViewController')

driver.scroll(original_ele, destination_ele)

destination_ele.click()