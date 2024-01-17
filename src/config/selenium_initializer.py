from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from models.record_data import *
import re

class SeleniumInitializer:

    def get_driver(self, url: str) -> webdriver:
        '''
        Returns Selenium driver with Url
        '''
        # instantiate options 
        options = webdriver.ChromeOptions() 

        # run browser in headless mode 
        # options.headless = True 
        options.add_argument('--headless')

        # instantiate driver 
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 

        # url = 'https://music.apple.com/cm/album/gangsta-for-life-the-symphony-of-david-brooks/1273792563'
        # url = 'https://music.apple.com/cm/album/art-and-life/723518371'
        # url = 'https://music.apple.com/cm/album/simma/1704435473'
        # url = 'https://music.apple.com/cm/album/we-caa-done-single/1661424383'
        # url = 'https://music.apple.com/cm/album/soca-gold-2020/1520406357'

        driver.get(url) 
        return driver