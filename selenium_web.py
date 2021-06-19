#for automation processs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")#--->to open  chrome 
    
    
    def get_info(self,query):#---------------------------------------------------------------------->query=item to search in web
        self.query = query
        self.driver.get(url=" https://www.wikipedia.org/ ")#------------------------------------>open url
        search = self.driver.find_element_by_xpath(' //*[@id="searchInput"] ')#--------------------->path of search bar 
        search.click()#---------------------------------------------------------------------------->to click 
        search.send_keys(query)#------------------------------------------------------------------->enter the search variable
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button ')#------->path of search button
        enter.click()#----------------------------------------------------------------------------->to click
        while(True):#------------------------------------------------------------------------------->to stop automatic close of web browser
            pass

assist = inflow()
assist.get_info("cars")#---------------------------------------------------------------------------->to enter the element to search