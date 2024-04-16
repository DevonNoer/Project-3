# Popular Spotify Songs

## Introduction

Our group created an ETL pipeline and SQL database schema. With Jupyter Notebooks, we used Python to import our data, export the cleaned data into separate tables, design table schema for the database, and import the data into PostgreSQL using pgAdmin.

In addition, we built an API using Flask and SQLAlchemy that can allow the data from SQL to be queried into python.

## About The Data

The dataset is Top Spotify Songs by Kumar Arnav on Kaggle. Each row of the data is a popular song on Spotify, and contains the song name, the names and number of artists, and the date of release, and the number of streams on Spotify.

The dataset also contains the following for each song:

- Number of times the song is in playlists: Spotify, Apple, Deezer
- The rank of the song in charts: Spotify, Apple, Deezer Shazam
- Tempo (beats per minute), key, and mode (major or minor)s
- Musical Characteristics: Danceability, valence, energy, acousticness, instrumentalness, liveness, speechiness

## Importing and Cleaning

We downloaded the dataset as a csv file and brought it into a python notebook using the pandas library. This allowed us to easily view the data and see how it was structured. We also used pyjanitor, a library that allowed multiple data cleaning functions to be performed with fewer lines of code.

With both of these libraries, our data cleaning included:

- Dropping n/a values
- Renaming columns
- Concatenate the Year, Month, and Day columns into a single Date column using the DateTime library
- Dropping the Year, Month, and Day columns as they will not be needed for the database
- Sorting the data by the number of Spotify streams

For each table we wanted from the dataset, we made filtered the data into separate dataframes, and reindexed each dataframe to give each row a unique identifier. After this, we exported csv files from each table.

## Designing the ERD and Database Schema

![Image](Project-3%20Spotify/Pictures/Spotify%20ERD.png)

**Above: Our Entity-Relationship-Diagram**

We used quickdatabasediagrams.com to design an Entity-Relationship-Diagram (ERD) that shows how our database is structured. Each tables attributes, datatypes, primary and foreign keys, and one-to-one relationships can be seen in this diagram.

## Importing the Data into PostgreSQL

We created the database structure that we outlined in our ERD. The csv files were imported into each respective table schema. Shown below are images showing the data in all of the images.

### Charts Table
![Image](Project-3%20Spotify/Pictures/charts.png)

### Date Table
![Image](Project-3%20Spotify/Pictures/date.png)

### Music Characteristics Table
![Image](Project-3%20Spotify/Pictures/music_char1.png)
![Image](Project-3%20Spotify/Pictures/music_char2.png)

### Playlist Table
![Image](Project-3%20Spotify/Pictures/playlist.png)

### Track Table
![Image](Project-3%20Spotify/Pictures/track1.png)
![Image](Project-3%20Spotify/Pictures/track2.png)

## Developing the API with Flask and SQLAlchemy

## Ethical Considerations

While our group does not foresee serious ethical implications, we do acknowledge possible biases that could be in the data.

- We don't know how exactly the songs in this dataset were chosen from Spotify. While we know that they were generally chosen based on streams and popularity, we don't know the complete information of Spotify's music library.

- A song could have a high number of streams, playlists, or chart rankings, because it was already popular before. Put another way, sometimes people like to listen to songs because they are already popular. This in turn could cause a feedback loop.

- We didn't examine the demographics of the artists, charts, or playlists in this dataset. Further examination could show possible biases.

- Because this dataset deals with current popular music, possible biases in the data could also be a reflection of the music industry as a whole.

## References

Top Spotify Songs by Kumar Arnav on Kaggle: https://www.kaggle.com/datasets/arnavvvvv/spotify-music
pyjanitor Documentation: https://pyjanitor-devs.github.io/pyjanitor/api/functions/