#for automation processs
from selenium import webdriver

class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")#--->to open  chrome 
    
    def get_info(self,query):#---------------------------------------------------------------------->query=item to search in web
        self.query=query
        self.driver.get(url="https://en.wikipedia.org")#-------------------------------------------->open url
        while(True):
            pass 

assist = inflow()
assist.get_info("hello")