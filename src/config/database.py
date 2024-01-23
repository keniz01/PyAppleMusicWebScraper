import sqlalchemy as db
import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config.logger import Logger as logger
from dotenv import load_dotenv

load_dotenv()
Base = automap_base()

user_name = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port_number = os.getenv("DB_PORT_NUMBER")
database_name = os.getenv("DB_NAME")
server_name = os.getenv("DB_SERVER")

try:
    engine = db.create_engine(f'postgresql://{user_name}:{password}@{server_name}:{port_number}/{database_name}')
    Base.prepare(autoload_with=engine)
    session = Session(engine)
except Exception as err:
    logger.logError("Cannot connect to DB %s", err)
    raise err  

def save_data(record_data_rows: list ):
    '''
    Saves records to database
    '''
    Record = Base.classes.staging
    rows = []

    for record_data_row in record_data_rows:
        row = Record(
            primary_artist = record_data_row.primary_artist,
            primary_artist_type = record_data_row.primary_artist_type,
            featured_artist = record_data_row.featured_artist,
            featured_artist_type = record_data_row.featured_artist_type,
            album_title = record_data_row.album_title,
            album_release_year = record_data_row.album_release_year,
            album_genre = record_data_row.album_genre,
            album_sub_genre = record_data_row.album_sub_genre,
            album_label = record_data_row.album_label,
            album_type = record_data_row.album_type,
            is_compilation_album = record_data_row.is_compilation_album,
            track_title = record_data_row.track_title,
            track_length_mins = record_data_row.track_length_mins,
            track_position = record_data_row.track_position,
            track_genre = record_data_row.track_genre,
            track_label = record_data_row.track_label
        )

        rows.append(row)

    try:
        session.add_all(rows)    
        session.commit()
    except Exception as err:
        session.rollback()
        logger.logError("Cannot insert rows to DB: %s", err)
        raise err    