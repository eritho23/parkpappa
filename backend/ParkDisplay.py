from flask import Flask, jsonify, abort
import json

app = Flask(__name__)

# Load parks data from the JSON file
def load_parks():
    with open("ParkCache.json", "r", encoding="utf8") as f:
        return json.load(f)
    
@app.route('/api/parks', methods=['GET'])
def GetParks():
    parks = load_parks()  # Load the data from the file
    return jsonify(parks)  # Return the parks data as a JSON response

@app.route('/api/parks/<int:id>', methods=['GET'])
def get_park_by_id(id):
    parks = load_parks()  # Load the data from the file
    for park in parks:
        if park.get("Id") == id:
            return jsonify(park)  # Return the found park data as JSON
   
if __name__ == '__main__':
    app.run()
