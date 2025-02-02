"""
    Main Flask app for the Park API. Contains the Flask logic regarding routes,
    methods, headers etc. It also handles caching.

    Author: David Lockley
"""
from flask import Flask, jsonify, render_template, request
import requests
import json
import threading
import time
from . import CoordinatesConverter
#import CoordinatesConverter
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # This allows all origins to access your API

CACHE_FILE = "ParkCache.json"
LINKS_FILE = "ParkLinks.json"  # Add your links.json file path here

def scrape_data():
    url = "https://kartor.vasteras.se/arcgis/rest/services/ext/tk_lekplatser_dyn/FeatureServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:97161.8,%22ymin%22:6596631.56,%22xmax%22:203248.2,%22ymax%22:6635410.44,%22spatialReference%22:{%22wkid%22:3010}&geometryType=esriGeometryEnvelope&inSR=3010&outFields=*&returnIdsOnly=false&returnCountOnly=false&geometryPrecision=2&outSR=3010"
    try:
        response = requests.get(url)
        raw_data = response.json()  # Parse JSON data

        features = raw_data.get('features', [])

        equipment_mapping = {
            "BBQArea": "GRILL",
            "ClimbingFrame": "KLATTERLEK",
            "RunningTrack": "FARTLEK",
            "SandPlayArea": "SANDLEK",
            "SwingSet": "GUNGLEK",
            "WaterAvailability": "VATTEN",
            "RainShelter": "REGNSKYDD",
            "SleddingHill": "PULKABACKE",
            "WindShelter": "VINDSKYDD",
        }

        play_types_mapping = {
            "BalancingPlay": "BALANSLEK",
            "CarPlay": "FORDONSLEK",
            "HopscotchArea": "HOPPLEK",
            "RockingPlay": "VAGGLEK",
            "RolePlay": "ROLLEK",
            "SlidePlay": "RUTSCHLEK",
            "SoundPlay": "LJUDLE",
            "SpinningPlay": "SNURRLEK",
            "ToddlerPlay": "PYSSELEK",
            "WaterPlay": "VATTENLEK",
            "PlayCircuit": "LEKSLINGA",
        }

        organized_data = []

        for idx, feature in enumerate(features):
            attributes = feature.get('attributes', {})
            geometry = feature.get('geometry', {})

            equipment = {
                title: (True if attributes.get(key, "NEJ") == "JA" else False)
                for title, key in equipment_mapping.items()
            }

            play_types = {
                title: (True if attributes.get(key, "NEJ") == "JA" else False)
                for title, key in play_types_mapping.items()
            }

            try:
                CordsWGS = CoordinatesConverter.ConvertToWGS(geometry.get("x"), geometry.get("y"))
                Ycord = CordsWGS[0]
                Xcord = CordsWGS[1]
            except:
                print("ERROR: CANT GET CORDS")
                Ycord = 0
                Xcord = 0

            organized_data.append({
                "Id": idx,
                "Name": attributes.get("NAMN", "N/A"),
                "Coordinates": {
                    "x": Xcord,
                    "y": Ycord
                },
                "Equipment": equipment,
                "TypesOfPlay": play_types
            })

        with open(CACHE_FILE, "w", encoding="utf8") as f:
            json.dump(organized_data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error during scraping: {e}")

def load_parks():
    try:
        with open(CACHE_FILE, "r", encoding="utf8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{CACHE_FILE} not found. Scraping data...")
        scrape_data()  
        with open(CACHE_FILE, "r", encoding="utf8") as f:
            return json.load(f)

def load_links():
    try:
     with open(LINKS_FILE, "r", encoding="utf8") as f:
            return json.load(f)
    except:
        print("Error: loading embed file")

@app.route('/api/parks', methods=['GET'])
def get_parks():
    parks = load_parks()
    return jsonify(parks)

@app.route('/api/parks/<int:id>', methods=['GET'])
def get_park_by_id(id):
    parks = load_parks()
    for park in parks:
        if park.get("Id") == id:
            return jsonify(park)
    return jsonify({"error": "Park not found, Make sure you input a valid ID"}), 404

@app.route('/api/parks/random', methods=['GET'])
@app.route('/api/parks/random/<int:amount>', methods=['GET'])
def get_random_parks(amount=3):  # Default amount set to 3
    parks = load_parks()
    if amount > len(parks):
        return jsonify({"error": "Requested amount exceeds available parks"}), 400
    
    random_indices = random.sample(range(len(parks)), amount)  # Get unique random indices
    random_parks = [parks[i] for i in random_indices]          # Fetch parks based on random indices
    
    return jsonify(random_parks)

@app.route('/api/parks/<int:id>/embed', methods=['GET'])
def get_park_embed(id):
    links = load_links()
    embed = next((item for item in links if item["Id"] == id), None)
    if embed:
        return(embed["Link"])
    return jsonify({"error": "Embed not found for this park ID"}), 404


@app.route('/', methods=['GET'])
def intro_screen():
    return render_template("index.html")

@app.route('/api/parks/search', methods=['POST'])
def search_parks():
    search_criteria = request.json
    if not search_criteria:
        return jsonify([]), 200

    parks = load_parks()
    filtered_parks = []

    for park in parks:
        matches = True
        for key, value in search_criteria.items():
            # Check if the key exists in park data and matches the value
            if not (key in park.get("Equipment", {}) and park["Equipment"][key] == value) and not (key in park.get("TypesOfPlay", {}) and park["TypesOfPlay"][key] == value):
                matches = False
                break
        if matches:
            filtered_parks.append(park)
    # Return the filtered parks or an empty list if no matches are found
    return jsonify(filtered_parks), 200

@app.route('/api/parks/random_filtered', methods=['POST'])
def get_random_parks_filtered():
    data = request.json
    include = data.get("include", {})
    exclude = data.get("exclude", {})
    amount = data.get("amount", 1)

    parks = load_parks()
    filtered_parks = []

    for park in parks:
        matches = True

        # If include is not empty, apply the include filters
        if include:
            for key, value in include.items():
                if not (key in park.get("Equipment", {}) and park["Equipment"][key] == value) and not (key in park.get("TypesOfPlay", {}) and park["TypesOfPlay"][key] == value):
                    matches = False
                    break

        # Always apply the exclude filters
        if matches:
            for key, value in exclude.items():
                if (key in park.get("Equipment", {}) and park["Equipment"][key] == value) or (key in park.get("TypesOfPlay", {}) and park["TypesOfPlay"][key] == value):
                    matches = False
                    break

        if matches:
            filtered_parks.append(park)

    random_parks = random.sample(filtered_parks, min(len(filtered_parks), amount))
    return jsonify(random_parks), 200



def run_gunicorn():
    import os
    from gunicorn.app.wsgiapp import run
    # Default Gunicorn arguments (customize as needed)
    os.environ.setdefault("GUNICORN_CMD_ARGS", "--workers 3 --bind 0.0.0.0:8000")
    # Pass your app module to Gunicorn
    run(["gunicorn", "app.ParkApi:app"])
