
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')
#driver = webdriver.Ie('C:\Users\skashem\Desktop\IEDriverServer\IEDriverServer')

# Go to URL
driver.get("http://www.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

# Sign-Up
driver.find_element_by_xpath("//*[@id='opt-signup']").click()
driver.find_element_by_id("email_address").send_keys("Email0012345@totsy.com")
driver.find_element_by_id("password").send_keys("user123")
driver.find_element_by_id("confirmation").send_keys("user123")
driver.find_element_by_id("submit-button").click()
driver.implicitly_wait(30)

#ignore send invite popup
driver.find_element_by_xpath("//*[@id='invitationForm']/div[2]/button/div").click()

#click on totsy logo
driver.find_element_by_xpath("//*[@id='logo']/a/img").click()

#click on an event
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='events-live']/ul/li[13]").click()

#choose the item
#driver.find_element_by_xpath("//*[@id='mainContent']/section/div[2]/div/ul/li[8]/div/a/img").click()

#log-out
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()


# Close Browser
driver.close()

