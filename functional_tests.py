from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.browser = webdriver.Firefox(options=options)


    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away
        #[...rest of comments as before]

if __name__ == '__main__':  
    unittest.main()
