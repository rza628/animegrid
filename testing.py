import requests
import sys
import time
import json
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

file = open('top1000.json', 'r', encoding=encoding)
top1000 = json.load(file)['top1000']
""" 
res = collectStats(top1000)
out = open('stats.json', 'w', encoding=encoding)
json.dump(res, out, indent=2) """


 
 