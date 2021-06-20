#for automation processs in youtube
from selenium import webdriver


class yt_data():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")  
        self.driver.maximize_window()
    
    def get_vedio(self,query):
        self.query = query
        self.driver.get(url=" https://www.youtube.com/results?search_query= " + query)
        vedio = self.driver.find_element_by_xpath(' //*[@id="video-title"]/yt-formatted-string')  
        vedio.click() 
        
        while(True):
          pass
    

