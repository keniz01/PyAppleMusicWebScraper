CREATE DATABASE discography
GO
create table staging
(
	id int primary key IDENTITY(1,1),
	primary_artist nvarchar(250),
	primary_artist_type nvarchar(250) check(primary_artist_type in ('SOLO', 'GROUP', 'BAND', '')),
	featured_artist nvarchar(250),
	featured_artist_type nvarchar(250) check(featured_artist_type in ('SOLO', 'GROUP', 'BAND', '')),
	album_title nvarchar(250),
	album_release_year int,
	album_genre nvarchar(250),
	album_label nvarchar(250),
	album_type nvarchar(250) check(album_type in ('MIXTAPE','EP','ALBUM','LP', 'SINGLE', '')),
	is_compilation_album bit,
	album_sub_genre nvarchar(250),
	track_title nvarchar(250),
	track_length_mins time,
	track_position int,
	track_genre nvarchar(250),
	track_label nvarchar(250),
	CONSTRAINT UC_staging UNIQUE (primary_artist,album_title,track_title)
)