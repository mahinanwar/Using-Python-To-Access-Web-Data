#Scraping Numbers from HTML using BeautifulSoup In this assignment you will
#write a Python program similar to http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in
#the file.
#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_695758.html (Sum ends with 53)
#You do not need to save these files to your folder since your program will read
#the data directly from the URL. Note: Each student will have a distinct data
#url for the assignment - so only use your own data url for analysis.
#You are to find all the <span> tags in the file and pull out the numbers from
#the tag and sum the numbers.
#Look at the sample code provided. It shows how to find all of a certain kind of
#tag, loop through the tags and extract the various aspects of the tags.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

my_url = input('Enter - ')

my_html = urllib.request.urlopen(my_url).read()
my_soup = BeautifulSoup(my_html,'html.parser')
tag = my_soup('span')
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print(count)
print(sum)
