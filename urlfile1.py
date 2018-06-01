import urllib2
# file = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
file = urllib2.urlopen('http://www.12123.com/news/36640.html')
message=file.read()
print message
