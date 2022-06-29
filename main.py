from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]  # to check the expensive first

for i in range(5001):
	actions = ActionChains(driver)
	actions.click(cookie)
	actions.perform()

	count = int(cookie_count.text.split(" ")[0])
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()
