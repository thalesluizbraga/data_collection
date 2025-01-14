#%%
import os
import json
import datetime
import requests
import pandas as pd

#%%

# funcao para acessar a api
def get_response(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print('Acesso na API deu erro')

# funcao para salvar json
def save_json(response, save_path):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')
    #response['ingestion_date'] = datetime.datetime.now()
    with open (f'{save_path}/{now}.json', 'w', encoding='utf-8') as j:
        json.dump(response,j, indent=4)

# funcao para puxar o json da raw e salvar um df pra trabalhar na silver
def save_df(raw_path):
    raw_path = save_path
    for file_name in os.listdir(raw_path):
        file_path = os.path.join(raw_path, file_name)
        
        if file_name.endswith('.json'):
            df = pd.read_json(file_path)
            return df 
        else:
            print('Nao havia arquivo para ser adicionado em json')

#%%

# Chamada das funcoes
url = 'https://pokeapi.co/api/v2/pokemon'
save_path = '../pokemon/raw/'
response = get_response(url)
save_json(response=response, save_path=save_path)



#%%

# falta condição de data aqui... se current_date > last date no diretorio




# proximos passos 
    # ingerir o json da raw, salvar em df e explodir ele
    # colocar na ingestao inicial do json e tambem no df uma condiça de data ingestao > data ultima ingestao




# Transform 
#df = pd.DataFrame(response)
#df_exploded = pd.json_normalize(df['results'])
#df = df.drop(columns='results').join(df_exploded)



# %%

df = pd.read_json('../pokemon/raw/teste.json')
df

 %%
