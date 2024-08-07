import requests
from sqlalchemy import create_engine

def fetch_api_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data = response.json()
    return data

import pandas as pd

def cleanse_data(api_data):
    # Convert API data to DataFrame
    df_api = pd.DataFrame(api_data)
    # Example cleansing: drop unnecessary columns
    df_api_clean = df_api[['userId', 'id', 'title', 'body']]
    
    
    return df_api_clean


def store_data(df_api, df_web):
    # Database connection string
    DATABASE_URI = 'postgresql+psycopg2://data_user:password@localhost/data_collection_db'
    engine = create_engine(DATABASE_URI)
    
    # Store API data
    df_api.to_sql('api_data', engine, if_exists='replace', index=False)
    
    # Store web data
    df_web.to_sql('web_data', engine, if_exists='replace', index=False)


api_data = fetch_api_data()
cleaned_data = cleanse_data(api_data)

print(cleaned_data.head())