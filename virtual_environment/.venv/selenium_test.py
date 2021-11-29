from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title())

search=driver.find_element_by_name("s")
search.send_Keys("test")
search.send_Keys(Keys.RETURN)

main=driver.find_element_by_id("main")
print(main.text)

try:
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

finally:
  driver.quit()

articles=main.find_element_by_tag_name("article")
for article in articles:
  header=article.find_element_by_class_name("entry-summary")
  print(header.text)




time.sleep(5)
driver.quit()
#to quit the browser driver.quit()
#to only close it driver.close()
#print(driver.title) it will print the title