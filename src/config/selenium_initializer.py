from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from models.record_data import *
import time

class SeleniumInitializer:
    '''
    Initialises selenium ready for use.
    '''

    def get_driver(self, url: str) -> webdriver:
        '''
        Returns Selenium driver with Url
        '''
        # instantiate options 
        options = webdriver.FirefoxOptions() 

        # run browser in headless mode 
        options.add_argument('--headless')

        try:
            # instantiate driver 
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options) 

            driver.get(url) 
            time.sleep(5)
            
            return driver
        except Exception as err:
            raise err