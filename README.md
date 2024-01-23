A Web scraping to specialises in scraping music records from the Apple Music website.
* The app uses requests to connect to https://music.apple.com.
* It then uses Selenium to inspect the page context and extract required data (Tried pandas and BeautifulSoup from bs4 but they dont work with dynamic data)
* We then use pyodbc to connect to a database table and save the extracted info.

.venv/bin/python ./src/main.py ./artefacts/test_data.csv