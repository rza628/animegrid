from flask import Flask, json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/animetitles", methods=["GET"])
def animetitles():
    titles = open("../anime_titles_nodupes.txt", "r", encoding='utf-8')
    titles = titles.read().strip().split('\n')
    formatList = []
    for entry in titles:
        split = entry.split(',')
        title, id = split[0], split[1]
        formatList.append({"title":title, "id":id})
    message = json.jsonify({"titles": formatList})
    return message
    
 