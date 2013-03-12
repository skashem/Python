from selenium import webdriver #importing selenium to python tool
from selenium.webdriver.common.keys import Keys #all the modes and methods i'm importing from selenium to python tool
from selenium.webdriver import ActionChains #performing actions
import time


# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver') # i'm using chrome instead of fire fox so that's the execution file where i saved it
#driver = webdriver.Ie('C:\Users\skashem\Desktop\IEDriverServer\IEDriverServer')

# Go to URL
driver.get('http://staging.totsy.com/')

# Implicit wait time
driver.implicitly_wait(30)

# Login Credentials
time.sleep(2)
#driver.find_element_by_css_selector("#email").send_keys(Keys.BACK_SPACE)
driver.find_element_by_css_selector("#email").send_keys("skashem+0965@totsy.com")
driver.find_element_by_css_selector("#pass").send_keys("user123")
driver.find_element_by_css_selector("#submit-button").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()

#Click on boys apparel
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div/div[1]/ul/li[1]/div/a/img").click()
driver.find_element_by_xpath("//*[@id='attribute169']").click()

#select size
driver.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[3]/form/div[2]/div[2]/fieldset/div/div[2]/div/select/option[2]").click()

#add to cart
driver.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[3]/form/div[2]/div[2]/div/div/button").click()

#checkout
driver.find_element_by_xpath("//*[@id='items-info-wrapper']/div[2]/div[2]/a").click()

#backspace to clear the item on QTY field
driver.find_element_by_xpath("//*[@id='qty-0']/div/div[1]/input").send_keys(Keys.BACK_SPACE)

#enter the QTY
driver.find_element_by_xpath("//*[@id='qty-0']/div/div[1]/input").send_keys(2)

#updating shopping cart
driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div[3]/form/table/tbody/tr/td/button").click()

#proceed to checkout
driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/div[4]/div/div[2]/button").click()

#choose credit card type
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_type']/input[2]").click()

#click on cc number field
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_number']").click()

#enter cc number
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_number']").send_keys("4111111111111111")

#click on cvn field
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_cid']").click()

#enter cvn number
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_cc_cid']").send_keys(123)

#click on expiration month
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration']").click()
#select expiration month
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div[3]/div/div[3]/div[3]/div/div[2]/div/select/option[2]").click()

#click on expiration year
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration_yr']").click()
#select expiration year
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div[3]/div/div[3]/div[3]/div/div[2]/div[2]/select/option[6]").click()

#uncheck the save cc box
driver.find_element_by_xpath("//*[@id='paymentfactory_tokenize_saved']").click()

#click on select address list
driver.find_element_by_xpath("//*[@id='billing-address-select']").click()
#select an address from drop down list
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/span/select/option[2]").click()

#click on ship to this address
#driver.find_element_by_xpath("//*[@id='button_ship_to']").click()

#Mouse hover to Place Order
Place_Order = driver.find_element_by_xpath("//*[@id='placeOrderBtn']")
hover = ActionChains(driver).move_to_element(Place_Order)
hover.perform()
#placing order
driver.find_element_by_xpath("//*[@id='placeOrderBtn']").click()

time.sleep(5)
#Mouse hover to Place Order
Place_Order = driver.find_element_by_xpath("//*[@id='placeOrderBtn']")
hover = ActionChains(driver).move_to_element(Place_Order)
hover.perform()
#placing order
driver.find_element_by_xpath("//*[@id='placeOrderBtn']").click()

time.sleep(10)

#log-out
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()

#Close Browser
driver.close()
