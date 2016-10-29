import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0

tags = soup('span')
for tag in tags:
    sum = sum + int(tag.text)
print sum

