from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Load the JSON data from the file
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Route to display all embeds
@app.route('/')
def display_all_embeds():
    data = load_json_file('ParkLinks.json')  # Replace with your actual JSON file
    
    return render_template_string("""
        <html>
            <head>
                <title>Embeds</title>
                <script async src="https://www.instagram.com/embed.js"></script>
            </head>
            <body>
                <h1>Park Embeds</h1>
                <ul>
                    {% for item in data %}
                        <li>
                            <h2>{{ item.Name }}</h2>
                            {% if item.Link %}
                                {{ item.Link | safe }}
                            {% else %}
                                <p>No link available for this item.</p>
                            {% endif %}
                        </li>
                    {% endfor %}
                </ul>
            </body>
        </html>
    """, data=data)

if __name__ == "__main__":
    app.run(debug=True)
