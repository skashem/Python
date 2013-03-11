from selenium.webdriver.common.keys import Keys #all the modes and methods i'm importing from selenium to python tool
from selenium.webdriver import ActionChains #performing actions
import time
from contextlib import closing
from selenium.webdriver import Chrome

Browser = Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')
url = 'http://staging.totsy.com/'

def Input_Field(Field_name,Field_value):
    Browser.find_element_by_xpath(Field_name).send_keys(Field_value)

def Link(Link_Name):
    Browser.find_element_by_xpath(Link_Name).click()

Browser.get(url)
#Log-in Credential
Input_Field("//*[@id='email']","skashem@totsy.com")
Input_Field("//*[@id='pass']",'skashem3422')
Link("//*[@id='submit-button']")

#Mouse hover to SHOP BY CATEGORY
shop_by_category = Browser.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(Browser).move_to_element(shop_by_category)
hover.perform()

#Click on boys apparel
Link("//*[@id='navByCat']/ul/li[2]/a")
Link("//*[@id='mainContent']/div[2]/div/div[1]/ul/li[1]/div/a/img")
Link("//*[@id='attribute169']")

#select size
Link("/html/body/div/div/section/div/div[2]/div[3]/form/div[2]/div[2]/fieldset/div/div[2]/div/select/option[2]")

#add to cart
Link("/html/body/div/div/section/div/div[2]/div[3]/form/div[2]/div[2]/div/div/button")

#checkout
Browser.find_element_by_xpath("//*[@id='header-checkoutBtn']").click()

#backspace to clear the item on QTY field
Browser.find_element_by_xpath("//*[@id='qty-0']/div/div[1]/input").send_keys(Keys.BACK_SPACE)

#enter the QTY
Input_Field("//*[@id='qty-0']/div/div[1]/input", 2)

#updating shopping cart
Link("//*[@id='mainContent']/div[2]/div[3]/form/table/tbody/tr/td/button")

#proceed to checkout
Link("//*[@id='header-checkoutBtn']/a")

#choose credit card type
Link("//*[@id='paymentfactory_tokenize_cc_type']/input[2]")

#click on cc number field
Link("//*[@id='paymentfactory_tokenize_cc_number']")

#enter cc number
Input_Field("//*[@id='paymentfactory_tokenize_cc_number']", "4111111111111111" )

#click on cvn field
Link("//*[@id='paymentfactory_tokenize_cc_cid']")

#enter cvn number
Input_Field("//*[@id='paymentfactory_tokenize_cc_cid']", 123)

#click on expiration month
Browser.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration']").click()
#select expiration month
Browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div[3]/div/div[3]/div[3]/div/div[2]/div/select/option[2]").click()

#click on expiration year
Browser.find_element_by_xpath("//*[@id='paymentfactory_tokenize_expiration_yr']").click()
#select expiration year
Browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div[3]/div/div[3]/div[3]/div/div[2]/div[2]/select/option[6]").click()

#uncheck the save cc box
Browser.find_element_by_xpath("//*[@id='paymentfactory_tokenize_saved']").click()

#click on select address list
Browser.find_element_by_xpath("//*[@id='billing-address-select']").click()
#select an address from drop down list
Browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div/span/select/option[2]").click()

#click on ship to this address
#driver.find_element_by_xpath("//*[@id='button_ship_to']").click()

#Mouse hover to Place Order
Place_Order = Browser.find_element_by_xpath("//*[@id='placeOrderBtn']")
hover = ActionChains(Browser).move_to_element(Place_Order)
hover.perform()
#placing order
Browser.find_element_by_xpath("//*[@id='placeOrderBtn']").click()

time.sleep(5)
#Mouse hover to Place Order
Place_Order = Browser.find_element_by_xpath("//*[@id='placeOrderBtn']")
hover = ActionChains(Browser).move_to_element(Place_Order)
hover.perform()
#placing order
Browser.find_element_by_xpath("//*[@id='placeOrderBtn']").click()

time.sleep(13)

#log-out
Browser.find_element_by_xpath("//*[@id='userAccount']/a").click()
Browser.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()

#Close Browser
Browser.close()



