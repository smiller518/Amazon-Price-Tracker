import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Apple-Generation-Lightning-Resistant-Headphones/dp/B0BDHB9Y8H/ref=sr_1_2_sspa?crid=2ZLWYSGX3CYTS&keywords=airpods&qid=1701115756&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sprefix=airpods%2Caps%2C79&sr=8-2-spons&ufe=app_do%3Aamzn1.fos.304cacc1-b508-45fb-a37f-a2c47c48c32f&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

headers = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)

bs = BeautifulSoup(page.content,'html.parser')

print(bs.prettify().encode("utf-8"))