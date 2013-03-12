from selenium import webdriver #importing selenium to python tool
from selenium.webdriver.common.keys import Keys #all the modes and methods i'm importing from selenium to python tool
from selenium.webdriver import ActionChains #performing actions
import time

Browser = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')
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


