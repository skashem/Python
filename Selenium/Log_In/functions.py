
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from practice import Edit_Field
# Instantiate Firefox browser
driver = webdriver.Chrome('C:\Users\skashem\Desktop\chromedriver\chromedriver')
# Go to URL
driver.get("http://staging.totsy.com")

# Implicit wait time
driver.implicitly_wait(30)

#Login Credentials
Edit_Field("//*[@id='email']", "skashem+0965@totsy.com")
Edit_Field("//*[@id='pass']", "user123")

