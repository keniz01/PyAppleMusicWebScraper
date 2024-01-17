from dataclasses import dataclass

@dataclass
class RecordData:
    primary_artist: str = ""
    primary_artist_type: str = ""
    featured_artist: str = ""
    featured_artist_type: str = ""
    album_title: str = ""
    album_release_year: int = 0
    album_genre: str = ""
    album_sub_genre: str = ""
    album_label: str = ""
    album_type: str = ""
    is_compilation_album: bool = False
    track_title: str = ""
    track_length_mins: str = ""
    track_position: int = 0
    track_genre: str = ""
    track_label: str = ""

