A Web scraping to specialises in scraping music records from the Apple Music website.
* The app uses requests to connect to https://music.apple.com.
* It then uses Selenium to inspect the page context and extract required data (Tried pandas and BeautifulSoup from bs4 but they dont work with dynamic data)
* We then use pyodbc to connect to a database table and save the extracted info.

In the artefacts folder, copy .env_file to the root folder and rename  it to `.env`. Replace the placeholder values with valid values.

Restore packages from the requirements.txt file using `py -m pip install -r ../artefacts/requirements.txt`

TRUNCATE staging RESTART IDENTITY
.venv/Scripts/activate
.venv/bin/python ./src/main.py ./artefacts/test_data.csv
