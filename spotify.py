from selenium import webdriver


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe") 
    
    
    def get_info(self,query):
        self.query = query
        self.driver.get(url='https://open.spotify.com/search')
        search = self.driver.find_element_by_xpath(' //*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input ') 
        search.click()
        search.send_keys(self.query)
        search.submit()
        select = self.driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[3]/button')
        select.click()
        
        
        while(True):
            pass

assist = music()
assist.get_info("closer")