import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		print("setup")
		self.driver = webdriver.Chrome("C:/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver.exe")
		self.driver.get('http://www.python.org')

	def test_example(self):  # starting with "test" means automaticaly starts
		print("test")
		assert False

	def test_example_2(self):
		assert True

	def not_a_test(self):
		print("this wont print")

	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
