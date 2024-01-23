-- Create database
CREATE DATABASE discography;

-- Create staging table
CREATE TABLE IF NOT EXISTS staging
(
	id SERIAL PRIMARY KEY,
	primary_artist VARCHAR(250),
	primary_artist_type VARCHAR(250) CHECK(primary_artist_type IN ('SOLO', 'GROUP', 'BAND', '')),
	featured_artist VARCHAR(250),
	featured_artist_type VARCHAR(250) CHECK(featured_artist_type IN ('SOLO', 'GROUP', 'BAND', '')),
	album_title VARCHAR(250),
	album_release_year INT,
	album_genre VARCHAR(250),
	album_label VARCHAR(250),
	album_type VARCHAR(250) CHECK(album_type IN ('MIXTAPE','EP','ALBUM','LP', 'SINGLE', '')),
	is_compilation_album BOOLEAN,
	album_sub_genre VARCHAR(250),
	track_title VARCHAR(250),
	track_length_mins TIME,
	track_position INT,
	track_genre VARCHAR(250),
	track_label VARCHAR(250),
	CONSTRAINT UC_staging UNIQUE (primary_artist,album_title,track_title)
);