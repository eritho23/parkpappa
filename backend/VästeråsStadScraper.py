from flask import Flask, jsonify
import requests
import json


app = Flask(__name__)
@app.route('/', methods=['GET'])
def scrape_data():
    url = "https://kartor.vasteras.se/arcgis/rest/services/ext/tk_lekplatser_dyn/FeatureServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:97161.8,%22ymin%22:6596631.56,%22xmax%22:203248.2,%22ymax%22:6635410.44,%22spatialReference%22:{%22wkid%22:3010}&geometryType=esriGeometryEnvelope&inSR=3010&outFields=*&returnIdsOnly=false&returnCountOnly=false&geometryPrecision=2&outSR=3010"
    try:
        response = requests.get(url)
        raw_data = response.json()  # Parse JSON data

        # Organize the data into a more readable format
        features = raw_data.get('features', [])
        organized_data = []
        for feature in features:
            attributes = feature.get('attributes', {})
            geometry = feature.get('geometry', {})
            organized_data.append(
                "Name": attributes.get("NAMN", "N/A"),
                "Equipment": [
                    "Bollek": attributes.get("BOLLEK", "null"),
                    "Fartlek": attributes.get("FARTLEK", "null"),
                    "Grill": attributes.get("GRILL", "null")},
                    "Gunglek": attributes.get("GUNGLEK", "null"),
                    "Hopplek": attributes.get("HOPPLEK", "null")

                    
                ],
                "Coordinates": {
                    "x": geometry.get("x", "N/A"),
                    "y": geometry.get("y", "N/A")
                }
            })
            # Save the organized data to a file
            with open("ParkCache.json", "w" , encoding="utf8") as f:
                json.dump(organized_data, f, indent=4, ensure_ascii=False)  # Pretty print the JSON

        return jsonify(raw_data['features'])          # Return data as a JSON response for Flask
    except:
        print("Det inte funkaj 😡")
    return response        
if __name__ == '__main__':
    app.run()
    
