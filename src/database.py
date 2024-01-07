import sqlalchemy as db
import logging
from sqlalchemy.engine import URL
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

driver='{SQL Server}'
server='localhost\SQLEXPRESS'
database='discography'
trusted_connection='yes'

connection_string = f'driver={driver};server={server};database={database};trusted_connection={trusted_connection}'
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
session = Session

try:
    engine = db.create_engine(connection_url,use_setinputsizes=False)
    Base.prepare(autoload_with=engine)
    session = Session(engine)
except OperationalError as err:
    logging.error("Cannot connect to DB %s", err)
    raise err  

def add_record(record_data_rows: list ):
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
    except OperationalError as err:
        logging.error("Cannot insert rows to DB %s", err)
        raise err  
      