#%%

# 1 - Imports
import time
import json
import datetime
import requests
import pandas as pd

# %%

# 2 - Functions

# get_response function
def get_response(url,**kwargs):
    response = requests.get(url, params=kwargs, verify=False)    
    return response

# save_file function
def save_file(save_path):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')
    with open(f'{save_path}{now}.json', 'w') as open_file:
        json.dump(data,open_file, indent=4)

# %%

# 3 - Extract and load

# Extract
url = 'https://www.tabnews.com.br/api/v1/contents/'

# Load
save_path = f'../tab_news/data/'
page = 1
while True:
    print(page)
    response = get_response(url, page=1, per_page=100, strategy='new')
    if response.status_code == 200:
        data = response.json()
        save_file(save_path=save_path)    
        if len(data) < 100:
            break
        page += 1
        time.sleep(2)
    else:
        print(response.status_code)
        print(response.json())
        time.sleep(60*5)

# %%

df = pd.read_json('../tab_news/data/2025-01-10_00-15-27.874463.json')
df
# %%
