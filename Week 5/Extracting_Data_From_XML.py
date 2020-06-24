#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read
#the XML data from that URL using urllib and then parse and extract the comment
#counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_695760.xml
#(Sum ends with 35)
#You do not need to save these files to your folder since your program will read
#the data directly from the URL. Note: Each student will have a distinct data
#url for the assignment - so only use your own data url for analysis.
#You are to look through all the <comment> tags and find the <count> values sum
#the numbers. The closest sample code that shows how to parse XML is geoxml.py.
#But since the nesting of the elements in our data is different than the data
#we are parsing in that sample code you will have to make real changes
#to the code.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

my_link = input('Enter location: ')
my_html = urllib.request.urlopen(my_link).read().decode()
print('Retrieving', my_link)
print('Retrieved', len(my_html), 'characters')

count = 0
sum = 0
data = ET.fromstring(my_html)
tags = data.findall('comments/comment')

for tag in tags:
    count += 1
    sum += int(tag.find('count').text)

print('Count:', count)
print('Sum:', sum)
