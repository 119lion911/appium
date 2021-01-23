from appium import webdriver
import time

######################################
# test using appium android emulator #
######################################
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0' # the android version of emulator device
desired_caps['deviceName'] = 'emulator-5554' # get with cmd: adb devices 
# desired_caps['appPackage'] = 'com.google.android.apps.nexuslauncher'
# desired_caps['appActivity'] = '.ConversationListActivity'
desired_caps['udid']='emulator-5554'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.start_activity("com.android.settings",".Settings") # package name, interface name
A=driver.find_elements_by_class_name("android.widget.LinearLayout") # use uiautomatoerviewer to find the element detail
A[6].click() # 6 is the index of the element
time.sleep(1)
driver.quit()
