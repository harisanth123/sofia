from selenium import webdriver
import wikipedia 

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
        
    def give_info(query):
        search_wiki = wikipedia.summary(query, sentences=2)
        print(search_wiki)
        return search_wiki
        
    while(True):
        pass
