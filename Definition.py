import re
import urllib.request
url = "http://dictionary.reference.com/browse/"
word = input ("Enter word to search: ")
url = url + word
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print (data1)

try:
	m = re.search('meta name="description" content=">', data1)
	start = m.end()
	end = start + 300
	newString = data1[start:end]

	print newString

	m = re.search('See more.', newString)
	end = m.start() - 1

	definition = newString[:end]

	print final
except:
	print "I'm sorry, your word is not in the dictionary"

