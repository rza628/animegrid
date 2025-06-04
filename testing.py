import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

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
""" data = fpl_api()['data'][1]
 
print(data['title']) """

file  = open('anime_titles.txt', 'w', encoding='utf-8')
data = malapi()
numPages = int(data['pagination']['last_visible_page'])
for i in range(1, numPages + 1):
    page = apiByPage(i)
    if (page):
        pageData = page['data']
        for anime in pageData:
            string = f'{anime['title']}, {anime['mal_id']}\n'
            file.write(string)
print('done')
            
 