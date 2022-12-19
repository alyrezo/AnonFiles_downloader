from bs4 import BeautifulSoup as bs
import requests, os, sys
soup = bs(requests.get(sys.argv[1]).text, "html.parser")
url = soup.find('a',id='download-url')['href']
os.system(f"aria2c -c -j1 -x16 -s16 -k1m -d /var/www/html --check-certificate=false {url}")
