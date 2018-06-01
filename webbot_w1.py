#import urllib

#image = urllib.URLopener()
#image.retrieve("http://www.mec.com.cn/News/18/228.html","imagefile.html")

import urllib2

file = urllib2.urlopen("http://www.mec.com.cn/News/18/228.html","imagefile.html")
message=file.read()
print (message)
