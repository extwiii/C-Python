import urllib
import xml.etree.ElementTree as ET

sum = 0
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = urllib.urlopen(address).read()
    tree = ET.fromstring(url)

    results = tree.findall('.//count')
    for result in results:
    	sum = sum + int(result.text)

    print sum

 
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553) 
# Actual data: http://python-data.dr-chuck.net/comments_320876.xml (Sum ends with 83)
