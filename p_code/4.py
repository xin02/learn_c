from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = r'D:\1.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()