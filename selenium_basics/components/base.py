from selenium.webdriver.common.by import By


# 0. Create a class Base
class Base:
    pass
#1. Add Constructor
    def __init__(self, driver):
        self.driver = driver
#2. Add click
    def click(self):
        item = self.driver.element_to_be_clickable(By.XPATH, "//*")
        item.click()
#4. Add method
    BASE_VAR = "Base Var"

