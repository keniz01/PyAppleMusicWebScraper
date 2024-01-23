import time
import pandas as pd
from config.database import save_data
from config.selenium_initializer import SeleniumInitializer
from page_content import PageContent
import sys

def main():

    selenium = SeleniumInitializer()

    try:

        file_path = sys.argv[1] 
        for chunk in pd.read_csv(file_path, chunksize=5):
            for url in chunk["Url"]:
                print(f"======= Processing Url -----> {url}")
                driver = selenium.get_driver(url)

                content = PageContent()
                content_list = content.extract_content(driver)

                try:
                    save_data(content_list)
                except: 
                    print("Error")
            time.sleep(10)
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print('An error occurred while reading the file')            
    except Exception as err:
        raise err


if __name__ == "__main__":
    main();