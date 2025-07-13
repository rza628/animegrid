import requests
import sys
import time
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
 
data = genres()
genrelist = []
for genre in data['data']:
    genrelist.append({'genre':genre['name']})
print(genrelist)

""" data = fpl_api()['data'][1]
 
print(data['title']) """

""" file  = open('anime_titles.txt', 'w', encoding='utf-8') """
""" file = open("new_anime_titles_delayed_call.csv", 'w', encoding='utf-8')
data = malapi()
numPages = int(data['pagination']['last_visible_page'])
for i in range(1, 1153, 1):
    page = apiByPage(i)
    if (page):
        pageData = page['data']
        for anime in pageData:
            string = f'{anime['title']}, {anime['mal_id']}\n'
            file.write(string)
    if (i % 3 == 0):
        time.sleep(1)
print('done') """
""" 
file = open('anime_titles.txt', 'r', encoding='utf-8')
file = file.read().strip().split('\n')
newfile = open('anime_titles_nodupes.txt', 'w', encoding='utf-8')
setNoDupe = set()
for pair in file:
    if pair not in setNoDupe:
        setNoDupe.add(pair)
        newfile.write(pair + '\n')
print('done') """
""" 
l1 = open('./anime_titles_nodupes.csv', 'r', encoding='utf-8').read().strip().split('\n')
l2 = open('./new_anime_titles_delayed_call.csv', 'r', encoding='utf-8').read().strip().split('\n')
l3 = open('./new_anime_titles.csv', 'r', encoding='utf-8').read().strip().split('\n')

file = open('combined_anime_titles.csv', 'w', encoding='utf-8')
check = set([])

for list in [l1, l2, l3]:
    for pair in list:
        if pair not in check:
            check.add(pair)
            file.write(pair + '\n')
        else:
            continue """





 