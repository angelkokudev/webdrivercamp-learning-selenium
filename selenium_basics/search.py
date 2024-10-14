# 1.Open Browser
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
print(driver.current_url)
driver.close()

# 2.Add wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
try:
    element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@id='gh-ac']")))
    print(driver.current_url)
finally:
    driver.quit()

# 3.Search items
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
try:
    element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@id='gh-ac']")))
    print(driver.current_url)
    element.send_keys("women watch")
    button = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    button.click()
finally:
    driver.quit()

# 4.Verify the search results
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
try:
    element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@id='gh-ac']")))
    print(driver.current_url)
    element.send_keys("women watch")
    button = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    button.click()
    header_content = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//span[@class='BOLD'][contains (text(), 'women watch')]")))
finally:
    driver.quit()

