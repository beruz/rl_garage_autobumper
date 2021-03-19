# -*- coding: utf-8 -*-
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


homepage_URL = 'https://rocket-league.com'

def get_credentials():     
        data = 'data.json'
        with open(data,'r') as f:
            user = json.load(f)
        return user

def enter_bump_time():
    while True:
        time = input('Enter bump timer in minutes (16 or more): ')
        try:
            val = int(time)
            if val>= 16:
                break
            else:
                print('Please enter a value 16 or more.')
        except ValueError:
            print('Input must be an integer')
    return val
                    
    
class Bumper:
    driver_path = "chromedriver.exe"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    user = {}  
    
    def login(self):
               
        self.driver.maximize_window()
        self.driver.get(homepage_URL)
        self.driver.find_element_by_id('acceptPrivacyPolicy').click()
        user = get_credentials()
        self.driver.find_element_by_id('header-email').send_keys(user['email'])
        self.driver.find_element_by_id('header-password').send_keys(user['password'])
        rememberme = self.driver.find_element_by_id('rememberme')
        self.driver.execute_script("arguments[0].click();", rememberme)
        login_btn = self.driver.find_element_by_xpath('.//input[@value="Go"]')
        login_btn.click()
        notif_btn = self.driver.find_element_by_id('declineNotifications')
        notif_btn.click()
          
    def tradePage(self):      
        
        username = self.driver.find_element_by_xpath('/html/body/header/section[1]/div/div[4]/div/a/span')
        username = username.text.lower()        
        trades_URL = homepage_URL + '/trades/' + username
        self.driver.get(trades_URL)
    
    def bumpTrades(self):
        trades_column = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div[3]')
        trades_list = trades_column.find_elements(By.CLASS_NAME,'rlg-trade')
        
        for trades in trades_list:
            bump = trades.find_element_by_xpath('.//button')
            bump_class = bump.get_attribute("class")
            if (bump_class == 'rlg-trade__action rlg-trade__bump --bump  is--disabled' ):
                timetxt = trades.find_element(By.CLASS_NAME, 'rlg-trade__time').text        
                for word in timetxt.split():
                    waitTime = 0
                    if word.isdigit():
                        ago = int(word)
                    if word == 'minutes':
                        waitTime = ago * 60                         
                        break
                    if word == 'seconds':   
                        waitTime += ago                         
                        break       
                waitTime = abs(float(waitTime - 960))        
                print('Wait for: ', waitTime/float(60)  , ' minutes to bump this trade...')                
            else:    
                bump.click()  
                print('Trade bumped successfully!')
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[2]/div').click()                    

    def refresh_site(self):
        self.driver.refresh()
                
def main():
    timer = enter_bump_time()
    bumper = Bumper()
    bumper.login()
    bumper.tradePage()    
    while(True):
        print('Bumping available trades...\n')
        bumper.bumpTrades()
        print('Sleeping for ', timer, ' minutes...')
        try:
            time.sleep(timer*60)
        except KeyboardInterrupt:
            print('Exitting program...')
            break
        bumper.refresh_site()      
    
    return 0
if __name__ == '__main__':
    main()
    