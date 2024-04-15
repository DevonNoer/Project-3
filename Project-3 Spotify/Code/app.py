# Import the dependencies.

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Users/ezrellemyhre-hager/Documents/GitHub/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to my app module Spotify ETL page!<br>"
        f"<br>"
        f"/api/v1.0/<start> - fetches spotify data from start date to most recent date in data."
        f"/api/v1.0/<start>/<end> - fetches spotify data from start date to end date in data."
    )

@app.route("/api/v1.0/<start>")
def spotify_data_start_end(start):
    session = Session(engine)

    # fetch data from start date to end date
    spotify_data = ""
    return jsonify(spotify_data)

@app.route("/api/v1.0/<start>/<end>")
def spotify_data_start_end(start, end):
    session = Session(engine)

    # fetch data from start date to end date
    spotify_data = ""
    
    return jsonify(spotify_data)


if __name__ == "__main__":
    app.run(debug=True)