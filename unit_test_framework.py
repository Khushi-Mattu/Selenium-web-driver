import unittest
from selenium import webdriver
import page 

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup") #This will be called every time test cases are run
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")
    
    def test_example(self):
        print("test")
        assert True

    def test_title(self):
        MainPage=page.MainPage()
        assert MainPage.is_title_matches()

    def not_a_test(self):
        print("this wont print")

    def test_search_in_python_org(self):
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
    
    def tearDown(self):
        self.driver.close()

    if __name__=="__main__":
        unittest.main()