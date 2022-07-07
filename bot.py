# https://sites.google.com/a/chromium.org/chromedriver/getting-started
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Instagram Bot Python Automation With Selenium - Deploy To PythonAnywhere

from selenium import webdriver
from time import sleep

class Bot():
    def __init__(self):
        self.login('','')
    
    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        
def main():
    my_bot = Bot()
    
if __name__ == '__main__':
    main()