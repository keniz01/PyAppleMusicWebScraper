from config.database import save_data
from config.selenium_initializer import SeleniumInitializer
from page_content import PageContent
import pandas as pd
import csv

def run():
    selenium = SeleniumInitializer()

    with open(r'C:\Users\kkiiza\source\demos\PyAppleMusicWebScraper\src\test.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['Url']
            driver = selenium.get_driver(url)
            content = PageContent()
            content_list = content.extract_content(driver)
            save_data(content_list)

if __name__ == "__main__":
    run()