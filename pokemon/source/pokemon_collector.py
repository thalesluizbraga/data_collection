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
def save_bronze(response, save_raw_path):
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')
    response['ingestion_date'] = now
    with open (f'{save_raw_path}{now}.json', 'w', encoding='utf-8') as j:
        json.dump(response,j, indent=4)

# funcao para puxar o json da raw e salvar um df pra trabalhar na silver
def save_df(raw_path):
    for file_name in os.listdir(raw_path):
        file_path = os.path.join(raw_path, file_name)
        
        if file_name.endswith('.json'):
            df = pd.read_json(file_path)
            return df 
        else:
            print('Nao havia arquivo para ser adicionado em json')


def transform_df(df):
    # Transform 
    df = pd.DataFrame(response)
    df_exploded = pd.json_normalize(df['results'])
    df = df.drop(columns='results').join(df_exploded)
    return df

def save_silver(df, save_silver_path, table_name):
    df.to_parquet(f'{save_silver_path}/{table_name}.parquet')

#%%

# Definicao de variaveis
url = 'https://pokeapi.co/api/v2/pokemon'
save_raw_path = 'pokemon/raw/'
save_silver_path = 'pokemon/silver/'
table_name = 'tb_pokemon_silver'

# Chamada das funcoes
response = get_response(url)
save_bronze(response=response, save_raw_path=save_raw_path)
df = save_df(raw_path=save_raw_path)
df = transform_df(df)
save_silver(df, save_silver_path = save_silver_path, table_name=table_name)



# Proximo passo
    # deixar modular os arquivos .py