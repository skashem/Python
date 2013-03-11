from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')

# Go to URL
driver.get("http://www.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

# Login Credentials
driver.find_element_by_css_selector("#email").send_keys("skashem@totsy.com")
driver.find_element_by_css_selector("#pass").send_keys("skashem3422")
driver.find_element_by_css_selector("#submit-button").click()

#Clicking on My Account Tab & Dashboard
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[1]/a").click()

#Mouse hover to Help Desk
Need_Help_Section = driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[2]/a")
hover = ActionChains(driver).move_to_element(Need_Help_Section)
hover.perform()
#click on Help Desk
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[2]/a").click()

time.sleep(10)

driver.back()
#Mouse hover to Faq's
Need_Help_Section = driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[3]/a")
hover = ActionChains(driver).move_to_element(Need_Help_Section)
hover.perform()
#click on FaQ
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[3]/a").click()

driver.back()
#Mouse hover to Privacy Policy
Need_Help_Section = driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[4]/a")
hover = ActionChains(driver).move_to_element(Need_Help_Section)
hover.perform()
#click on Privacy Policy
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[4]/a").click()

driver.back()
#Mouse hover Terms Of Use
Need_Help_Section = driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[5]/a")
hover = ActionChains(driver).move_to_element(Need_Help_Section)
hover.perform()
#click on Terms Of Use
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[2]/ul/li[5]/a").click()

#About Us
driver.get("https://www.totsy.com/pages/aboutus/")
#Mouse hover to How Totsy Works
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[2]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on How Totsy Works
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[2]/a").click()

#Mouse hover to Meet The Moms
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[3]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Meet The Moms
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[3]/a").click()

#Mouse hover to Totsy In The Press
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[4]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Totsy In The Press
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[4]/a").click()

#Mouse hover to Video Testimonials
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[5]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Video Testimonials
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[5]/a").click()

#Mouse hover to Being Green
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[6]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Being Green
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[6]/a").click()

#Mouse hover to Affiliate Program
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[8]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Affiliate Program
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[8]/a").click()

#Mouse hover to Careers
About_Us= driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[9]/a")
hover = ActionChains(driver).move_to_element(About_Us)
hover.perform()
#Click on Careers
driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/div/div[1]/div[1]/ul/li[9]/a").click()

#log out
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()

# Close Browser
driver.close()

