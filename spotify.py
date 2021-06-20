#for automation processs for spotify
from selenium import webdriver


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")#--->to open  chrome 
    
    
    def get_info(self,query):#---------------------------------------------------------------------->query=item to search in web
        self.query = query
        self.driver.get(url='https://open.spotify.com/search')#------------------------------------>open url
        search = self.driver.find_element_by_xpath(' //*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input ')#--------------------->path of search bar 
        search.click()
        search.send_keys(self.query)#------------------------------------------------------------------->enter the search variable
        search.submit()
        select = self.driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[3]/button')
        select.click()
        
        
        while(True):#------------------------------------------------------------------------------->to stop automatic close of web browser
            pass

assist = music()
assist.get_info("closer")