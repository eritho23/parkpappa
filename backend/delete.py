from flask import Flask, render_template_string, jsonify
import json

app = Flask(__name__)

# Load the JSON data from the file
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Route to get all items
@app.route('/')
def index():
    data = load_json_file('ParkLinks.json')  # Replace with your actual file path
    return render_template_string("""
        <html>
            <head><title>Embed Database</title></head>
            <body>
                <h1>Embed Database</h1>
                <ul>
                    {% for item in data %}
                        <li>
                            <strong>{{ item.Name }}</strong><br>
                            <a href="{{ item.Link }}" target="_blank">View on Instagram</a>
                        </li>
                    {% endfor %}
                </ul>
            </body>
        </html>
    """, data=data)

# Route to get a specific object by ID
@app.route('/item/<int:item_id>')
def get_item(item_id):
    data = load_json_file('your_file.json')  # Replace with your actual file path
    item = next((obj for obj in data if obj['Id'] == item_id), None)
    if item:
        return render_template_string("""
            <html>
                <head><title>{{ item.Name }}</title></head>
                <body>
                    <h1>{{ item.Name }}</h1>
                    <p>ID: {{ item.Id }}</p>
                    <p><a href="{{ item.Link }}" target="_blank">View this post on Instagram</a></p>
                </body>
            </html>
        """, item=item)
    else:
        return f"Item with ID {item_id} not found.", 404

if __name__ == "__main__":
    app.run(debug=True)
