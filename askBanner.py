import selenium
from selenium import webdriver




#makes chrome the browser
driver = webdriver.Chrome()

# goes the askbanner site
driver.get('https://aisapps.vassar.edu/askbanner/stuinfo.html')

# accesses the 999 id number the inputs mine id
id_box = driver.find_element_by_name('id')
id_box.send_keys('your_IDnumber')

#accesses the pin number and inputs my pin
pin_box = driver.find_element_by_name('pin')
pin_box.send_keys('your_pin_number')

#get login button and click
login_button = driver.find_elements_by_name('submit')[1]
login_button.click()
