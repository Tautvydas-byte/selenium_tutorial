from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

link = driver.find_element(By.LINK_TEXT,"Python Programming")
