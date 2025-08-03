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

 
file = open('top1000.json', 'r', encoding=encoding)

print(len(json.load(file)['top1000']))




 