import urllib
import json

sum = 0
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = urllib.urlopen(address).read()
    info = json.loads(str(url))

    
    for comment in info['comments']:
    	sum = sum + int(comment['count'])

    print sum

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553) 
# Actual data: http://python-data.dr-chuck.net/comments_320880.json (Sum ends with 15)