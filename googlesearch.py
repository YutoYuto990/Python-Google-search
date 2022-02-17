import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
# keyword to search
search_word = input(please).replace(" ","+").replace("　","+")

# how many content
pages_num=4

print(f'【word】{search_word}')

# Google page
url = f'https://www.google.co.jp/search?hl=ja&num={pages_num}&q={search_word}'
request = requests.get(url)

# Google page html
soup = BeautifulSoup(request.text, "html.parser")
search_site_list = soup.select('div.kCrYT > a')


for rank, site in zip(range(1, pages_num), search_site_list):
    try:
        site_title = site.select('h3.zBAuLc')[0].text
    except IndexError:
        site_title = site.select('img')[0]['alt']
    site_url = site['href'].replace('/url?q=', '')
    # result
    result=f"[{site_title}]({site_url})"
    q=result.find("&sa")
    #urldecode
    print(unquote(f"{result[:q]})"))
