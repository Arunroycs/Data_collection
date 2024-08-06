import requests

def fetch_api_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data = response.json()
    return data

fetch_api_data()