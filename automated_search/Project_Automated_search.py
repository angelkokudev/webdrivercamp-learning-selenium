from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, presence_of_all_elements_located
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#1.Open eBay watch page

driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

#2.Select option Brand / Rolex in Filter pane

element_rolex = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH,"//input[@aria-label='Rolex']")))
element_rolex.click()

#3.Verify the first two result items contain “rolex” in their title

item_1_title = wait.until(presence_of_element_located((By.XPATH,"//ul[@class='srp-results srp-grid clearfix']/li[position()=3]//span[@role='heading'][contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')]")))
item_2_title = wait.until(presence_of_element_located((By.XPATH,"//ul[@class='srp-results srp-grid clearfix']/li[position()=4]//span[@role='heading'][contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')]")))

#4.Store title and price of the first two results in a variable

item_1_price_element = wait.until(presence_of_element_located((By.XPATH,"//ul[@class='srp-results srp-grid clearfix']/li[position()=3]//span[@class='s-item__price']"))).text
item_2_price_element = wait.until(presence_of_element_located((By.XPATH,"//ul[@class='srp-results srp-grid clearfix']/li[position()=4]//span[@class='s-item__price']"))).text

item_1_price = float(item_1_price_element.replace("US", "").replace("$", "").replace(",", ""))
item_2_price = float(item_2_price_element.replace("US", "").replace("$", "").replace(",", ""))

#5.Open item in a new tab and verify the title and the price by comparing them with the stored

item_1_title.click()
driver.switch_to.window(driver.window_handles[1])

new_tab_title_1_element = wait.until(presence_of_element_located((By.XPATH,"//h1/span[@class='ux-textspans ux-textspans--BOLD']"))).text
new_tab_price_1_element = wait.until(presence_of_element_located((By.XPATH,"//div[@class='x-price-primary']/span[@class='ux-textspans']"))).text

new_tab_price_1 = float(new_tab_price_1_element.replace("US", "").replace("$", "").replace(",", ""))



item_1_title == new_tab_title_1_element
item_1_price == new_tab_price_1

# 6.Uncheck “Rolex“ option

driver.switch_to.window(driver.window_handles[0])

element_rolex = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']")))
element_rolex.click()

# 7.Check “Casio“ option

element_casio = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//input[@aria-label='Casio']")))
element_casio.click()

#8.Verify the last two result items contain "Casio" in their title

items = WebDriverWait(driver, 10).until(presence_of_all_elements_located((By.XPATH, "//li[@class='s-item s-item__pl-on-bottom']")))

items_length = len(items)
print(items_length)

if items:
    first_last_item = items[66]
    second_last_item = items[67]

#9.Save and print all the mismatches if any

non_casio_item = []
if 'casio' not in first_last_item.text.lower():
    non_casio_item.append(first_last_item.text)
if 'casio' not in second_last_item.text.lower():
    non_casio_item.append(second_last_item.text)
if non_casio_item:
    print(non_casio_item)

driver.quit()
