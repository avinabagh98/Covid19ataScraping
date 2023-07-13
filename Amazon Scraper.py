from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.amazon.in/'

response = requests.get(url)
print(response)                      # if response is 403 then pass header (refer ml 100 days playlist)

page = BeautifulSoup(response.content, 'html5lib')
print(page)