from flask import Flask, json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/animetitles")
def animetitles():
    titles = open("../combined_anime_titles.csv", "r", encoding='utf-8')
    titles = titles.read().strip().split('\n')
    #testing with only the first 2000
    formatList = []
    for entry in titles[:2000]:
        split = entry.rsplit(',', 1)
        title, id = split[0], split[1]
        formatList.append({"title":title, "id":id})
    message = json.jsonify({"titles": formatList})
    return message
    
 