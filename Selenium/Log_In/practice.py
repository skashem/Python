from Log_In import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains




#method fo send keys
def Edit_Field( user_name,password ):
    driver.find_element_by_xpath("//*[@id='email']").send_keys(user_name)
    return Edit_Field

#Login Credentials
#Edit_Field("//*[@id='email']", "skashem+0965@totsy.com")
#Edit_Field("//*[@id='pass']", "user123")
#click_on_objects("//*[@id='submit-button']")

#clicking on sign out
#click_on_objects("//*[@id='userAccount']/a")
#click_on_objects("//*[@id='userAccount']/ul/li[10]/a")




