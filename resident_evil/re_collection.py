#%%

# Imports
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# %%

# Funcoes

# get_content function
def get_content(url):
    response = requests.get(url, headers=headers, verify=False)
    return response

# get_basic_info function
def get_basic_infos(response):
    soup = BeautifulSoup(response.text)
    div_page = soup.find('div', class_='td-page-content')
    paragrafo = div_page.find_all('p')[1]
    ems = paragrafo.find_all('em')

    data = {}
    for i in ems:
        key,value, *_ = i.text.split(':') # Esse *_ é um unpack de lista.... entender melhor
        key = key.strip(' ')
        data[key] = value.strip(' ').replace('.', '')
    return data

# get_appearences function
def get_appearences(response):
    soup = BeautifulSoup(response.text)
    lis = (soup.find('div', class_='td-page-content')
                .find('h4')
                .find_next()
                .find_all('li') )

    appearences = [i.text for i in lis]
    return appearences

# e a mesma coisa disso aqui
#aparicoes = []
#for i in lis:
    #aparicoes.append(i.text)
#aparicoes

# get_characters_info function
def get_characters_info(url):
    response = get_content(url)
    if response.status_code != 200:
        print('Nao foi possivel obter os dados')
    else:
        data = get_basic_infos(response)
        data['appearences'] = get_appearences(response)    
    return data

# get_characters_links function
def get_characters_links():
    response = requests.get(url_characters, headers=headers, verify=False)
    soup = BeautifulSoup(response.text)
    anchors = (soup.find('div', class_='td-page-content').
                find_all('a'))
    links = [i['href'] for i in anchors]
    return links


# %%

# Chamada das funcoes e definicoes de variaveis
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://www.residentevildatabase.com/personagens/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
url = 'https://www.residentevildatabase.com/personagens/ada-wong/'
url_characters = 'https://www.residentevildatabase.com/personagens'

get_characters_info(url)
get_characters_links()

# %%

links = get_characters_links()
data = []
for i in tqdm(links):
    d = get_characters_info(i)
    d['link'] = i
    data.append(d)

# %%
data

# %%
