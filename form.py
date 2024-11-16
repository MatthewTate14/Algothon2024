# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
driver = webdriver.Chrome()

# Open URL
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeUYMkI5ce18RL2aF5C8I7mPxF7haH23VEVz7PQrvz0Do0NrQ/')
#
# # wait for one second, until page gets fully loaded
# time.sleep(1)
#
# # check the checkbox
# checkbox = driver.find_element_by_xpath(
# 	'//*[@id="i9"]/div[3]/div')
# checkbox.click()
#
# #fill in the text box with text data which is a string
#
#
# # click on submit button
# submit = driver.find_element_by_xpath(
# 	'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
# submit.click()
#
# # fill another response
# another_response = driver.find_element_by_xpath(
# 	'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
# another_response.click()

# close the window
# driver.quit()
