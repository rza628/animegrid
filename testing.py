import requests
import sys
import time
import json
import random
sys.stdout.reconfigure(encoding='utf-8')
encoding = 'utf-8'
def malapi():
    url = 'https://api.jikan.moe/v4/anime'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except:
        return None

def apiByPage(page):
    url = f'https://api.jikan.moe/v4/anime?page={page}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except:
        return None
    #getting title

def genres():
    url = 'https://api.jikan.moe/v4/genres/anime'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except:
        return None
    
def getTitleSynonyms(id):
    url = f'https://api.jikan.moe/v4/anime/{id}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['data']['title_synonyms']:
                return data['data']['title_synonyms']
            else:
                return []
    except:
        return None

def genres():
    stats = {'genres':[], 'explicit_genres':[], 'themes':[],"demographics":[]}

    for enum in stats.keys():

        url = f'https://api.jikan.moe/v4/genres/anime?filter={enum}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            data = sorted(data['data'], key= lambda x: x['count'], reverse=True)
            stats[enum] = data
    return stats

def getTop(n):
    topN = {'top1000':[]}
    for i in range(1, n + 1):
        url = f'https://api.jikan.moe/v4/top/anime?page={i}'
        response = requests.get(url)
        data = response.json()
        data = data['data']
        for entry in data:
            name, id = entry['title'], entry['mal_id']
            topN['top1000'].append({"name":name, "id":id})
        time.sleep(0.75)
    return json.dumps(topN, indent=2)

def collectStats(data):

    template = {"genres":{}, "themes":{}, "explicit_genres":{}, "demographics":{}, "studios":{}, "source":{}, "season":{} }
    it = 0
    for entry in data:
        it += 1
        id = entry['id']
        url = f'https://api.jikan.moe/v4/anime/{id}'
        response = requests.get(url)
        res = response.json()
        res = res["data"]
        
        if res['season'] not in template['season']:
            template['season'][res['season']] = 1
        else:
            template['season'][res['season']] += 1

        if res['source'] not in template['source']:
            template['source'][res['source']] = 1
        else:
            template['source'][res['source']] += 1

        for studio in res['studios']:
            if studio['name'] not in template['studios']:
                template['studios'][studio['name']] = 1
            else:
                 template['studios'][studio['name']] += 1

        for genre in res['genres']:
            if genre['name'] not in template['genres']:
                template['genres'][genre['name']] = 1
            else:
                 template['genres'][genre['name']] += 1

        for exGenre in res['explicit_genres']:
            if exGenre['name'] not in template['explicit_genres']:
                template['explicit_genres'][exGenre['name']] = 1
            else:
                 template['explicit_genres'][exGenre['name']] += 1

        for theme in res['themes']:
            if theme['name'] not in template['themes']:
                template['themes'][theme['name']] = 1
            else:
                 template['themes'][theme['name']] += 1

        for demo in res['demographics']:
            if demo['name'] not in template['demographics']:
                template['demographics'][demo['name']] = 1
            else:
                 template['demographics'][demo['name']] += 1
    
        time.sleep(0.75)
        if it % 50 == 0:
            print(template)
    return template

file = open('stats.json', 'r', encoding=encoding)
top1000 = json.load(file)

# genres : 2415
# themes : 1640
# explicit_genres : 0
# demographics : 516
# studios : 1053
# source : 1000
# season : 1000

# for now, removing 'themes', 'explicit_genres'
sample = ['genres', 'demographics', 'studios', 'source']

acrossProbs = [6, 1.5, 2, 3]
chosen = random.choices(sample, weights=acrossProbs, k=3)
cats = []
 
for choice in chosen:
    probs =  top1000[choice].values()
    randomChoice = random.choices(list(top1000[choice].keys()),weights=list(probs), k=1)[0]
    cats.append({"type":choice, "category":randomChoice})
print(cats)

#doing down topics now
downTopics = [ "Episodes", "Year", "Airing Status", "Mal Score", "Mal Rank"]
chosen = random.choices(downTopics, k=3)
downCats = []
for choice in chosen:
    randomChoice = None
    if choice == "Episodes":
        possibilities = ["<=13", ">=13", ">=20", "50+"]
        randomChoice = random.choices(possibilities, k=1)[0]
    elif choice == "Year":
        possibilities = ["1970 - 1985", "1985 - 1990", "1990 - 2000","2000 - 2005","2005 - 2010", "2015 - 2020", "2020 - 2025", "2025 - 2030"]
        randomChoice = random.choices(possibilities, k=1)[0]
    elif choice == "Airing Status":
        # removed not yet aired option
        possibilities = ["Finished Airing", "Currently Airing"]
        randomChoice = random.choices(possibilities, k=1)[0]
    elif choice == "Mal Score":
        possibilities = [">=8.5", ">=8", ">=7.5", ">=7"]
        randomChoice = random.choices(possibilities, k=1)[0]
    elif choice == "Mal Rank":
        possibilities = ["1 - 100", "101 - 200", "201 - 500", "501 - 1000"]
        randomChoice = random.choices(possibilities, k=1)[0]
    downCats.append({"type":choice, "category":randomChoice})

print(downCats)

"""     if choice == "season":
        randomChoice = random.choices(list(top1000['season'].keys()), weights=list(top1000['season'].values()), k=1)[0]
        if randomChoice == None:
            downCats.append({"type":"Any", "category":randomChoice})
        else:
        downCats.append({"type":choice, "category":randomChoice}) """