import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://edition.cnn.com/travel/article/sports-car-with-wings-icon-a5/index.html'))

for img in soup.find_all("img", src=True):
    print(img["src"])