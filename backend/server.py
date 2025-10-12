from flask import Flask, json
import requests, random, unicodedata
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
    
@app.route("/api/categories/<date>")
def categories(date):
    #status, finished, airing, upcoming
    #got studios and split genres to genres, explicit, themes, demographics, used weighted random choice
    # also use rankings, and scores, rankings are based on anime score on mal
    # episode count, season, year (before or after some year like 2010), soruce
    """ def genres():
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

    categories = random.sample(genres, 6) """
    data = getRandCategories(date)
    # sample ["Action", "Romance", "Superpower", "Mystery", "Supernatural", "Comedy"]
    # data = [{"type":"genres", "category":"Action"},{"type":"source", "category":"Manga"}
    #                                        ,{"type":"demographics", "category":"Shounen"},{"type":"Year", "category":"2006 - 2010"},
    #                                        {"type":"Episodes", "category":"<=13"},{"type":"Airing Status", "category":"Finished Airing"}]
    message = json.jsonify({"categories": data})
    return message

def getRandCategories(date):
    random.seed(date)
    file = open('../stats.json', 'r', encoding='utf-8')
    top1000 = json.load(file)

    #got rid of studios, themes, explicit, 
    sample = ['genres', 'demographics', 'source']

    acrossProbs = [6, 1.5, 3]
    chosen = []
    while len(chosen) < 3:
        randChoice = random.choices(sample, weights=acrossProbs, k=1, )
        if randChoice not in chosen:
            chosen.append(randChoice[0])
    cats = []
    
    for choice in chosen:
        probs =  top1000[choice].values()
        randomChoice = random.choices(list(top1000[choice].keys()),weights=list(probs), k=1)[0]
        cats.append({"type":choice, "category":randomChoice})

    #doing down topics now, got rid of Mal Rank, seasons
    downTopics = [ "Episodes", "Year", "Airing Status", "Mal Score"]
    chosen = random.sample(downTopics, k = 3)
    downCats = []
    for choice in chosen:
        randomChoice = None
        if choice == "Episodes":
            possibilities = ["<=13", ">=13", ">=20", "50+"]
            randomChoice = random.choices(possibilities, k=1)[0]
        elif choice == "Year":
            possibilities = ["1970 - 1985", "1986 - 1990", "1991 - 2000","2001 - 2005","2006 - 2010", "2011 - 2015", "2016 - 2020", "2021 - 2025", "2026 - 2030"]
            randomChoice = random.choices(possibilities, k=1)[0]
        elif choice == "Airing Status":
            # removed not yet aired option
            possibilities = ["Finished Airing", "Currently Airing"]
            randomChoice = random.choices(possibilities, k=1)[0]
        elif choice == "Mal Score":
            possibilities = [">=8.5", ">=8", ">=7.5", ">=7"]
            randomChoice = random.choices(possibilities, k=1)[0]
        """ elif choice == "Mal Rank":
            possibilities = ["1 - 100", "101 - 200", "201 - 500", "501 - 1000"]
            randomChoice = random.choices(possibilities, k=1)[0] """
        downCats.append({"type":choice, "category":randomChoice})

    return cats + downCats
@app.route('/api/search/<input>')
def search(input):
    titles = open("../combined_anime_titles.csv", "r", encoding='utf-8')
    titles = titles.read().strip().split('\n')
    filteredTitles = []
    for entry in titles:
        split = entry.rsplit(',', 1)
        title, id = split[0], split[1]
        if input in title.lower():
            filteredTitles.append({"title":title, "id":id})
    message = json.jsonify({'data':filteredTitles})
    return message

