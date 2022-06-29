from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://techwithtim.net')

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
	)
	element.click()
	button = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "sow-button-19310003"))
	)
	button.click()

	driver.back()#back to previuos page
	driver.back()
	driver.back()
	driver.forward()
	driver.forward()
except:
	driver.quit()
