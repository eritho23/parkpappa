from flask import Flask, jsonify
import requests
import json
import threading
import time
import schedule
from . import CoordinatesConverter
#import CoordinatesConverter
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # This allows all origins to access your API

CACHE_FILE = "ParkCache.json"

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


@app.route('/', methods=['GET'])
def intro_screen():
    return "Yoooo use the URL /api/parks"

def schedule_scrape():
    schedule.every().day.at("00:00").do(scrape_data)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    if not load_parks():
        scrape_data()
    threading.Thread(target=schedule_scrape, daemon=True).start()
    #app.run() # Commented out as Gunicorn will handle the app execution
    app.run(host='0.0.0.0', port=5000)