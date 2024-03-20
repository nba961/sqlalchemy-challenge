# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
stations = Base.classes.station
measurements = Base.classes.measurement
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def index():
    return 'Welcome!'

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def tobs():
    return jsonify(tobs)