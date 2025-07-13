from flask import Flask, json
import requests, random
from flask_cors import CORS

"flask --app server --debug run"
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
    for entry in titles:
        split = entry.rsplit(',', 1)
        title, id = split[0], split[1]
        formatList.append({"title":title, "id":id})
    message = json.jsonify({"titles": formatList})
    return message

def genres():
    url = 'https://api.jikan.moe/v4/genres/anime'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except:
        return None
    
@app.route("/api/categories")
def categories():
    def genres():
        url = 'https://api.jikan.moe/v4/genres/anime'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
        except:
            return None
    data = genres()
    data = data['data']
    genres = [entry['name'] for entry in data]

    categories = random.sample(genres, 6)
    message = json.jsonify({"categories": ["Action", "Romance", "Superpower", "Mystery", "Supernatural", "School"]})
    return message

