from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.facebook.com')
mail='mai'
name='e'+mail+'l'
uName= driver.find_element_by_id(name)
passwd= driver.find_element_by_id('pass')
uName.send_keys('arunkumar309@gmail.com')
passwd.send_keys('facebookyeah')
driver.find_element_by_id('u_0_x').click()
