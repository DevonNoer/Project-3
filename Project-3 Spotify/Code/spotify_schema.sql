-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "track" (
    "track_id" int   NOT NULL,
    "track" varchar(255)   NOT NULL,
    "artists" varchar(255)   NOT NULL,
    "artist_count" int   NOT NULL,
    "streams" float   NOT NULL,
    CONSTRAINT "pk_track" PRIMARY KEY (
        "track_id"
     )
);

CREATE TABLE "charts" (
    "chart_id" int   NOT NULL,
    "track_id" int   NOT NULL,
    "in_spotify_charts" int   NOT NULL,
    "in_apple_charts" int   NOT NULL,
    "in_deezer_charts" int   NOT NULL,
    "in_shazam_charts" int   NOT NULL,
    CONSTRAINT "pk_charts" PRIMARY KEY (
        "chart_id"
     )
);

CREATE TABLE "date" (
    "date_id" int   NOT NULL,
    "track_id" int   NOT NULL,
    "date" date   NOT NULL,
    CONSTRAINT "pk_date" PRIMARY KEY (
        "date_id"
     )
);

CREATE TABLE "music_characteristics" (
    "music_id" int   NOT NULL,
    "track_id" int   NOT NULL,
    "bpm" int   NOT NULL,
    "mode" varchar(255)   NOT NULL,
    "key" varchar(255)   NOT NULL,
    "danceability_%" int   NOT NULL,
    "valence_%" int   NOT NULL,
    "energy_%" int   NOT NULL,
    "acousticness_%" int   NOT NULL,
    "liveness_%" int   NOT NULL,
    "speechiness_%" int   NOT NULL,
    CONSTRAINT "pk_music_characteristics" PRIMARY KEY (
        "music_id"
     )
);

CREATE TABLE "playlist" (
    "playlist_id" int   NOT NULL,
    "track_id" int   NOT NULL,
    "in_spotify_playlists" int   NOT NULL,
    "in_apple_playlists" int   NOT NULL,
    "in_deezer_playlists" int   NOT NULL,
    CONSTRAINT "pk_playlist" PRIMARY KEY (
        "playlist_id"
     )
);

ALTER TABLE "charts" ADD CONSTRAINT "fk_charts_track_id" FOREIGN KEY("track_id")
REFERENCES "track" ("track_id");

ALTER TABLE "date" ADD CONSTRAINT "fk_date_track_id" FOREIGN KEY("track_id")
REFERENCES "track" ("track_id");

ALTER TABLE "music_characteristics" ADD CONSTRAINT "fk_music_characteristics_track_id" FOREIGN KEY("track_id")
REFERENCES "track" ("track_id");

ALTER TABLE "playlist" ADD CONSTRAINT "fk_playlist_track_id" FOREIGN KEY("track_id")
REFERENCES "track" ("track_id");

SELECT * FROM charts;
SELECT * FROM date;
SELECT * FROM music_characteristics;
SELECT * FROM playlist;
SELECT * FROM track;