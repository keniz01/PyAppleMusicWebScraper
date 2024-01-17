from selenium import webdriver 
from selenium.webdriver.common.by import By 
from models.record_data import *
import re

class PageContent:

    def extract_content(self, driver: webdriver) -> list:

        '''
        Extract values from page content elements
        '''
        album_name_element = driver.find_element(By.CLASS_NAME,'headings__title')
        album_name = album_name_element.text

        primary_artist_list_element = driver.find_element(By.CLASS_NAME, 'headings__subtitles')
        primary_artist_list = primary_artist_list_element.text

        genre_element = driver.find_element(By.CLASS_NAME, 'headings__metadata-bottom')
        genre = genre_element.text.strip().split()[0]

        description_element = driver.find_element(By.XPATH, "//p[@data-testid='tracklist-footer-description']")
        last_line_break = description_element.text.rfind('\n')
        description = description_element.text[last_line_break:]
        description_arr = description.replace(',', ' ', 1).split(' ', 1)[1].split()
        year = description_arr[0]

        description_arr.pop(0)
        label = ' '.join(description_arr, )

        track_list = driver.find_elements(By.CLASS_NAME, 'songs-list-row')

        return self.get_tabulated_data(track_list, album_name, genre, year, label, primary_artist_list)
    
    def get_tabulated_data(self, 
                           track_list: list, 
                           album_name: str,
                           genre: str, 
                           year: int, 
                           label: str,
                           primary_artist_list: list) -> list:
        '''
        Constructs and returns a tabulised list of data from the page content
        '''
                
        record_data_rows = []

        for track in track_list: 	
            track_title_element = track.find_element(By.CLASS_NAME, 'songs-list-row__song-name')
            track_length_mins = track.find_element(By.CLASS_NAME, 'songs-list-row__length')
            track_title = track_title_element.text if track_title_element.text.count('feat.') == 0 else re.split('\((.*?)\)', track_title_element.text)[0].rstrip()
            featured_artist_list = [] if track_title_element.text.count('feat.') == 0 else re.split('\((.*?)\)', track_title_element.text)[1].replace('feat. ', '').replace(' &', ',').split(',')
            featured_artists = '' if len(featured_artist_list) == 0 else ', '.join(featured_artist_list)
            
            track_position = track.find_element(By.CLASS_NAME, 'songs-list-row__column-data').text
            album_compilation_element = track.find_elements(By.CLASS_NAME, 'songs-list-row__by-line')
            is_compilation_album = len(album_compilation_element) > 0
            
            record_data = RecordData(
                primary_artist = primary_artist_list if is_compilation_album == False else "Various Artists",
                primary_artist_type = 'SOLO',
                featured_artist = featured_artists if is_compilation_album == False else album_compilation_element[0].text,
                featured_artist_type = 'SOLO' if len(featured_artist_list) == 1 else '' if len(featured_artist_list) == 0 else 'GROUP',
                album_title = album_name,
                is_compilation_album = is_compilation_album,
                album_release_year = year,
                album_genre = genre,
                album_label = label,
                album_type = 'SINGLE' if len(track_list) == 1 else 'ALBUM',
                track_title = track_title,
                track_length_mins = f'0{track_length_mins.text}',
                track_position = track_position,
                track_genre = genre,
                track_label = label
            )

            record_data_rows.append(record_data)
            
        return record_data_rows