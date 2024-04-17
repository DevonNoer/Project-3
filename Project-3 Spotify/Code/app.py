from flask import Flask, jsonify
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import json 

app = Flask(__name__)

@app.route('/')
def welcome():
    welcome_message = """
    <h1>Welcome to the Spotify ETL API!</h1>
    <p>This API provides various JSON data for each table in our spotify database. Also some extra routes to show other functionalities.</p>
    <h2>Available Routes:</h2>
    <ul>
        <li><a href="/charts">/charts</a>: Returns JSON data for the charts table.</li>
        <li><a href="/date">/date</a>: Returns JSON data for the date table.</li>
        <li><a href="/music_characteristics">/music_characteristics</a>: Returns JSON data for the music_characteristics table.</li>
        <li><a href="/playlist">/playlist</a>: Returns JSON data for the playlist table.</li>
        <li><a href="/track">/track</a>: Returns JSON data for the track table.</li>
        <li><a href="/songs/2021-01-01/2022-01-01">/songs/start_date/end_date</a>: Returns JSON data for the songs released in a date range. Ex. /songs/2021-01-01/2022-01-01 for the songs released in 2021.</li>
    </ul>
    """
    return welcome_message

# Function to fetch data from a table and return it as JSON
def fetch_table_data(table_name):
    # Connect to the database
    conn = pg.connect(host="localhost", port=5432,  dbname="spotify_db", user="postgres", password="postgres")
    cur = conn.cursor()

    # Execute the SELECT query
    cur.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows
    rows = cur.fetchall()

    # Close database connection
    cur.close()
    conn.close()

    # Convert data to JSON format
    return jsonify({table_name: rows})

# Define routes to return JSON data for each table
@app.route('/charts')
def json_charts():
    return fetch_table_data('charts')

@app.route('/date')
def json_date():
    return fetch_table_data('date')

@app.route('/music_characteristics')
def json_music_characteristics():
    return fetch_table_data('music_characteristics')

@app.route('/playlist')
def json_playlist():
    return fetch_table_data('playlist')

@app.route('/track')
def json_track():
    return fetch_table_data('track')

# Define route to get songs from a specific date range
@app.route('/songs/<start_date>/<end_date>')
def get_songs_by_date_range(start_date, end_date):
    connection = pg.connect("dbname=spotify_db user=postgres password=postgres")
    
    #Reading a query to get a table from postgres into pandas
    date_df = psql.read_sql_query("SELECT * FROM date", connection)
    track_df = psql.read_sql_query("SELECT * FROM track", connection)
    
    # Convert start_date and end_date to Timestamp objects
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    
    # Convert 'date' column in date_df to Timestamp objects
    date_df['date'] = pd.to_datetime(date_df['date'])
    
    # Filter songs released within the specified date range
    date_range = date_df[(date_df['date'] >= start) & (date_df['date'] <= end)]
    
    # Merge with track_df to include track names and artists
    songs_within_range = pd.merge(date_range, track_df[['track_id', 'track', 'artists']], on='track_id', how='left')

    # Convert DataFrame to JSON serializable format
    songs_json = songs_within_range.to_json(orient='records', indent=4)

    # Convert the JSON string to a dictionary
    songs_dict = json.loads(songs_json)

    # Return the pretty-printed JSON string using jsonify
    return jsonify(songs_dict)

if __name__ == '__main__':
    app.run(debug=True)