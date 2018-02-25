import re
import urllib.request
#url = https://www.google.com/finance?q=
url = "https://www.google.com/finance?q="
stock = input ("Enter your stock: ")
url = url + stock
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print (data1)
m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
print("\n " + newString)

m = re.search('content="',newString)
start = m.end()
newString1 = newString[start:]
print (newString1)
m = re.search("/",newString1)
end = m.start()-2
print ("The value of the " + stock + " stock is " + newString1[:end])