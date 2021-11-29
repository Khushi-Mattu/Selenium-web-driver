# Selenium
<p>
  First we have to download the web driver from chrome. Then first import webdriver from selenium. Then we have to specify the path of the webdriver. 
  </p>
  <p> We have to get the url by using driver.get("url"). To close the tab we can do driver.close() but to close the entire browser we have to use driver.quit(). we can get the title of the page by print(driver.title)</p>
  <h2>Locating elements from HTML </h2>
    <p> To search for something by name specifically, we can use search=driver.find_element_by_name(" ")</p>
    <p> from selenium.webdriver.common.keys import Keys. this gives access to keys like enter and escape keys </p>
    <p> search.send_keys("test") The string to be searched for.</p>
    <p>search.send_keys(Keys.RETURN)</p>
    <p>These three steps i.e 1. search=driver.find_element_by_name("s") 2. search.send_keys("test") 3. search.send_keys(Keys.RETURN)<p>
  <p>we found the search box (s), we typed in test and the pressed enter </p>
  </br>
  <p>To delay the program, we can use time.sleep(5) . It will basically not quit immediately </p>
  <p>print(driver.page_source) will print the page source code </p>
  <p> once we look at the source code of the website after searching for test, we will see that all of the search results are under a main tag. </p>
  <p> so to search for main we will use main=driver.find_element_by_id("main")</p>
  <p>print(main.text) will print to see what it is </p>
  <p> To wait for an explicit amount of time, we can use 
  try:
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
finally:
driver.quit()</p>
  <p>for this, we need some imports that are from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC </p>
<p> Instead of finally, except can be used if we want to quit only when it doesnt work </p>
<p> Now, we want to print the summary under all headers written of all the search results. So, we will inspect the code and see where all the headers are. We will notice they are all in articles. So, articles=main.find_element_by_tag_name("article").
  for article in articles:
    header=article.find_element_by_class_name("entry-summary")
  print(header.text)
  <h2>Page Navigating and clicking elements </h2>
  <p>Selenium has find_element_by_link_text(). It allows us to type the text that would show up from the link and access the element from that.</p>
  <p>link=driver.find_element_by_link_text("python programming") </p>
  <p>link.click() will open the link </p>
  <p>we will add a new explicit amount of time try: and finally where we change the By.ID to By.LINK_TEXT in try</p>
  <p>
  try:
  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
  element.click()
finally:
driver.quit()
  </p>
  <p>driver.back() is used for going to the previous page. </p>
  <p>driver.forward() to go to the next page. </p>
  <h2> ActionChains & Automating Cookie Clicker </h2>
  <p>Here, we are using this website https://orteil.dashnet.org/cookieclicker/ </p>
  <p> The first step is obviously importing so, from selenium.webdriver.common.action_chains import ActionChains. </p>
  <p>actions=ActionChains(driver)</p>
  <p> There is going to be a new ActionChains Object and it is going to act on the driver. </p>
  <p> actions.click() will click the mouse wherever it is and if we dont write actions.perform() nothing will happen. </p>
  <p>Now we want to count the number of cookies. </p>
  <p> cookie=driver.find_element_by_id("big cookie") </p>
  <p>cookie_count=driver.find_element_by_id("cookies") </p>
  <p>driver.implicitly_wait(5) this will make them to wait for 5 seconds before going to the next line. </p>
  
  
  


  
  
