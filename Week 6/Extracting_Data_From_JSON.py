#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the
#JSON data from that URL using urllib and then parse and extract the comment
#counts from the JSON data, compute the sum of the numbers in the file and enter
#the sum below:
#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_695761.json
#(Sum ends with 68)
#You do not need to save these files to your folder since your program will read
#the data directly from the URL. Note: Each student will have a distinct data
#url for the assignment - so only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
import json

my_link = input('Enter location: ')
print('Retrieving', my_link)

my_html = urllib.request.urlopen(my_link).read().decode()
print('Retrieved', len(my_html), 'characters')

try:
    js = json.loads(my_html)
except:
    js = None

count = 0
sum = 0
for item in js['comments']:
    count += 1
    sum += int(item['count'])

print('Count:', count)
print('Sum:', sum)
