# install using `pip3 install newsapi` (this project uses Python3)
#from newsapi import NewsApiClient
# from newsapi.newsapi_client import NewsApiClient
import requests

# REPLACE with your API key. collect from: https://newsapi.org/

#api = NewsApiClient(api_key='77950512b1c34bac828f32bd9e22e550')
# API Endpoints guide: https://newsapi.org/docs/endpoints/top-headlines
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'category=health&'
       'from=2023-06-16&'
       'sortBy=popularity&'
       'apiKey=77950512b1c34bac828f32bd9e22e550')

if __name__ == "__main__":
    response = requests.get(url)
    result = response.json()
    articles = result['articles']
    
    for article in articles[:3]:
        print("TITLE: ", article['title'], "DESC: ", article['description'])
