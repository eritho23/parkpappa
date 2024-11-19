from flask import Flask, jsonify
import requests
import json
from pyproj import Proj, transform
import CoordinatesConverter
app = Flask(__name__)
@app.route('/api/parks', methods=['GET'])
def scrape_data():
    url = "https://kartor.vasteras.se/arcgis/rest/services/ext/tk_lekplatser_dyn/FeatureServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:97161.8,%22ymin%22:6596631.56,%22xmax%22:203248.2,%22ymax%22:6635410.44,%22spatialReference%22:{%22wkid%22:3010}&geometryType=esriGeometryEnvelope&inSR=3010&outFields=*&returnIdsOnly=false&returnCountOnly=false&geometryPrecision=2&outSR=3010"
    try:
        response = requests.get(url)
        raw_data = response.json()  # Parse JSON data

        # Organize the data into a more readable format
        features = raw_data.get('features', [])

        # Define separate dictionaries for Equipment and Types of Play
        equipment_mapping = {
            "BBQ Area": "GRILL",
            "Climbing Frame": "KLATTERLEK",
            "Running Track": "FARTLEK",
            "Sand Play Area": "SANDLEK",
            "Swing Set": "GUNGLEK",
            "Water Availability": "VATTEN",
            "Rain Shelter": "REGNSKYDD",
            "Sledding Hill": "PULKABACKE",
            "Wind Shelter": "VINDSKYDD",

        }

        # Play types mapping (sorted alphabetically)
        play_types_mapping = {
            "Balancing Play": "BALANSLEK",
            "Car Play": "FORDONSLEK",
            "Hopscotch Area": "HOPPLEK",
            "Rocking Play": "VAGGLEK",
            "Role Play": "ROLLEK",
            "Slide Play": "RUTSCHLEK",
            "Sound Play": "LJUDLE",
            "Spinning Play": "SNURRLEK",
            "Toddler Play": "PYSSELEK",
            "Water Play": "VATTENLEK",
            "Play Circuit": "LEKSLINGA",
        }

        organized_data = []

        for idx, feature in enumerate(features):
            attributes = feature.get('attributes', {})
            geometry = feature.get('geometry', {})
            
            # Separate Equipment and Types of Play
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
            # Append the data
            organized_data.append({
                "Id": idx,
                "Name": attributes.get("NAMN", "N/A"),
                "Coordinates": {
                    "x": Xcord,
                    "y": Ycord
                },
                "Equipment": equipment,
                "Types of Play": play_types
            })

        # Sort the data alphabetically by "Name"

        # Save the organized data to a file
        with open("ParkCache.json", "w", encoding="utf8") as f:
            json.dump(organized_data, f, indent=4, ensure_ascii=False)  # Pretty print the JSON

        return jsonify(raw_data['features'])          # Return data as a JSON response for Flask
    except:
        print("Det inte funkaj 😡")
    return response        
if __name__ == '__main__':
    app.run()
    
