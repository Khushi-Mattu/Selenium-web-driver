# Selenium
<p>
  This is not a work of my own. This is only my interpretation of what I have learnt after watching the tutorial series and documentation whose links
  I have added in the bibliography.
  
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
  <p>items=[driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)] <p>
  <p> This will load all elements with id product price with string i.</p>
  <p> we want to upgrade cursor as much as grandma. But we will upgrade grandma first. </p>
  <p> actions.click(cookie) which is pressing that cookie </p>
  <p>for i in range(0,5000):
    actions.perform()
  This will basically do the action of clicking the cookies a 5000 times. </p>
  <p>
  for i in range(0,5000):
    actions.perform()
    count=int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value=int(item.text)
        if value<=count:
            upgrade_actions=ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
                        This will help to count the number of cookies and show the count. </p> 
  <h2> Unit Test Framework </h2>
  <p>
  We can use classes which contains the test cases we want that should be performed.
  We can put all variables or all the setup required in the def setup(self).
  self.driverwebdriver.Chrome(" PATH ")
  self.driver.get("url")
  The setup will run in the beginning.
  For the end,
  def tearDown(self):
    self.driver.close()
  def test_example():
  if we include this in between, it will run automatically.
  but if we write def not_a_test it wont run because it doesnt start with test.
  All this is because of unittest.
  </p>
  <p> if name=="_main_":
          unittest.main()
  This will run all the unit tests we have defined. </p>
  <p>The base page will be the base class for all of our pages.
  In this baseclass we will define a class for each page we will test.
  Locator.py is for any way we locate an element it should be in one place.
  We also dont have to change any other aspect of the code.
  Main page locators is a class for main page locators. All main page locators should come here.
  search results page locator is a class for search results locators. All search results locators should come here.
  element = self.driver.find_element(MainPageLocators.GO_BUTTON)
  Now here if I put a * in front of MainPageLocators,
  for example take a tuple (1,2) without * we re just passing (1,2) but with the * we are passing (*(1,2))
  Its called unpack.
  Base page class that is initialized on every page object class.
  __ __ is the dunder path which is part of python data model.
  </p>
  <p>In test_search_in_python_org, we first load the main page, then we assert the main page, then we will check if search text element is pycon
  then the click_go_button is to search for it, then it will give the search result page. Finally it will tell if we got any results.
  </p>
  
  <h2>Bibliography </h2>
  <p>
  1. https://selenium-python.readthedocs.io/installation.html (This is the documentation. It is not official but a great one to learn selenium from)<br/>
  2. https://www.youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ <br/>
  I learnt Selenium from these two and the tutorial playlist is awesome and so is the documentation. </p>
  
  
  
  
  


  
  
