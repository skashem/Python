from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from gg import account_tab
# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver') # i'm using chrome instead of fire fox so that's the execution file where i saved it

# Go to URL
url = driver.get("http://staging.totsy.com")

account_tab()
