import re

text = open('text.txt','r')
sum = 0
for line in text:
	digits = re.findall('[0-9]+',line)
	for digit in digits:
		sum = sum + int(digit)

print sum
