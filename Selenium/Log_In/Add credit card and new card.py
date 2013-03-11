from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')

# Go to URL
driver.get("http://staging.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

# Login Credentials
driver.find_element_by_css_selector("#email").send_keys("skashem@totsy.com")
driver.find_element_by_css_selector("#pass").send_keys("skashem3422")
driver.find_element_by_css_selector("#submit-button").click()

#adding new credit card
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[3]/a").click()
driver.find_element_by_xpath("//*[@id='mainContent']/div/div[3]/div/div[2]/div/h4/button[1]").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_type']").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[2]/div/div/div/form/div/div/div/div/select/option[3]").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_number']").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_number']").send_keys("5555555555554444")
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration']").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[2]/div/div/div/form/div/div/div[3]/div/div/select/option[6]").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration_yr']").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[2]/div/div/div/form/div/div/div[3]/div[2]/div/select/option[6]").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_cid']").click()
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_cid']").send_keys(345)

#log-out
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()

