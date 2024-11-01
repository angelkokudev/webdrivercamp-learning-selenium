from selenium import webdriver
from components.base import Base
driver = webdriver.Chrome
base = Base(driver)
print(dir(base))
