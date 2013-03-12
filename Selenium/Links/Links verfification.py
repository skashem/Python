from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')

# Go to URL
driver.get("http://www.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

# Login Credentials
driver.find_element_by_css_selector("#email").send_keys("skashem+0961@totsy.com")
driver.find_element_by_css_selector("#pass").send_keys("user123")
driver.find_element_by_css_selector("#submit-button").click()

#Mouse hover to All Sales
All_sales = driver.find_element_by_xpath("//*[@id='navAllEvents']/a/em")
hover = ActionChains(driver).move_to_element(All_sales)
hover.perform()
#click on new from All Sales
driver.find_element_by_xpath("//*[@id='navAllEvents']/ul/li[1]/a").click()

#Mouse hover to All Sales
All_sales = driver.find_element_by_xpath("//*[@id='navAllEvents']/a/em")
hover = ActionChains(driver).move_to_element(All_sales)
hover.perform()
#click on upcoming from All Sales
driver.find_element_by_xpath("//*[@id='navAllEvents']/ul/li[2]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Click on boys apparel
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[2]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Click on girls apparel
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[3]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#click on shoes
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[4]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#click on accessories
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[5]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Toys and Books
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[6]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Home
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[7]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Gear
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[8]/a").click()

#Mouse hover to SHOP BY CATEGORY
shop_by_category = driver.find_element_by_xpath("//*[@id='navByCat']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_category)
hover.perform()
#Moms and Dads
driver.find_element_by_xpath("//*[@id='navByCat']/ul/li[9]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#0-6M
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[2]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#6-24M
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[3]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#1-3Y
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[4]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#3-4Y
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[5]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#5+
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[6]/a").click()

#Mouse hover to SHOP BY AGE
shop_by_Age = driver.find_element_by_xpath("//*[@id='navByAge']/a/em")
hover = ActionChains(driver).move_to_element(shop_by_Age)
hover.perform()
#Adult
driver.find_element_by_xpath("//*[@id='navByAge']/ul/li[7]/a").click()

#Clicking on all the drop-down lists on My Account Tab
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[3]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[4]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[5]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[6]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[7]/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[8]/a").click()

#Click on My Account Tab
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
#Click on Dashboard
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[1]/a").click()

#Mouse hover to My TotsyPlus Membership
My_Totsy_Plus_Membership = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/ul/li[10]/a")
hover = ActionChains(driver).move_to_element(My_Totsy_Plus_Membership)
hover.perform()
#click on TotsyPlus Membership
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/ul/li[10]/a").click()

#log out
driver.find_element_by_xpath("//*[@id='userAccount']/a").click()
driver.find_element_by_xpath("//*[@id='userAccount']/ul/li[10]/a").click()

# Close Browser
driver.close()



