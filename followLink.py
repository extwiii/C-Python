import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
position = raw_input('Enter Position- ')
position = int(position)-1
count = raw_input('Enter Count - ')
count = int(count)
times = 0
# Retrieve all of the anchor tags
tags = soup('a')


while count > times :
	html1 = urllib.urlopen(url).read()
	soup1 = BeautifulSoup(html1)
	tags1 = soup1('a')
	url = tags1[position].get('href', None)
	times = times +1
	print url

# follow this link http://python-data.dr-chuck.net/known_by_Ines.html

