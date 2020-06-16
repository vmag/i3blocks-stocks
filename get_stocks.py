import requests
from bs4 import BeautifulSoup
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}

URL = sys.argv[1]
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

ticker = soup.find('span',class_='arial_22')
ticker_stock = soup.find('h1',class_='float_lang_base_1 relativeAttr')
actual = soup.find(id='fl_header_pair_lst')
change = soup.find(id='fl_header_pair_chg')
percent = soup.find(id='fl_header_pair_pch')

if float(percent.text.strip("%")) < 0:
    if ticker.text == None:
        print(ticker_stock.text.replace("&", "&amp;")+': '+'<span color=\'red\'>'+percent.text+'</span>')
    else:
        print(ticker.text.replace("&", "&amp;")+': '+'<span color=\'red\'>'+percent.text+'</span>')
else:
    print(ticker.text.replace("&", "&amp;")+': '+'<span color=\'#77e326\'>'+percent.text+'</span>')
    