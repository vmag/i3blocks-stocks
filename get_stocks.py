import requests
from bs4 import BeautifulSoup
import sys
import os
import notify2

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
notification_text = 'Actual: '+actual.text+'\n Change: '+change.text+'\n Percent change: '+percent.text

if float(percent.text.strip("%")) < 0:
    actual_text = '<span color=\'red\'>'+actual.text+'</span>'
    change_text = '<span color=\'red\'>'+change.text+'</span>'
    percent_text = '<span color=\'red\'>'+percent.text+'</span>'
else:
    actual_text = '<span color=\'#77e326\'>'+actual.text+'</span>'
    change_text = '<span color=\'#77e326\'>'+change.text+'</span>'
    percent_text = '<span color=\'#77e326\'>'+percent.text+'</span>'

notification_text = 'Actual: '+actual_text+'\n'+'Change: '+change_text+'\n'+'Percent: '+percent_text

if os.environ.get('BLOCK_BUTTON'):
    if (os.environ['BLOCK_BUTTON'] == '1'):
        n = notify2.init("Stocks and Futures")
        notification = notify2.Notification(ticker.text, notification_text, "dialog-information")
        notification.timeout = 3000
        notification.show()

if float(percent.text.strip("%")) < 0:
    if ticker.text is None:
        print(ticker_stock.text.replace("&", "&amp;")+': '+'<span color=\'red\'>'+percent.text+'</span>')
    else:
        print(ticker.text.replace("&", "&amp;")+': '+'<span color=\'red\'>'+percent.text+'</span>')
else:
    print(ticker.text.replace("&", "&amp;")+': '+'<span color=\'#77e326\'>'+percent.text+'</span>')



