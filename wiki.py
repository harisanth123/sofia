#for automation processs in WIKIPEDIA
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class wiki_data():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")  
        self.driver.maximize_window()
    
    def get_info(self,query):
        self.query = query
        self.driver.get(url=" https://www.wikipedia.org/ ")
        search = self.driver.find_element_by_xpath(' //*[@id="searchInput"] ')  
        search.click() 
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button ') 
        enter.click()
        while(True):
          pass

