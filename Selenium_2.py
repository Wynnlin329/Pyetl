from selenium.webdriver import Chrome
import requests
import time
url='https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&service=youtube&flowName=GlifWebSignIn&flowEntry=AddSession'

driver = Chrome('./chromedriver')

driver.get(url)

driver.find_element_by_id('identifierId').send_keys('summer54a21@gmail.com')
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_class_name('whsOnd').send_keys('33456789')
driver.find_element_by_id('passwordNext').click()



driver.find_element_by_partial_link_text()