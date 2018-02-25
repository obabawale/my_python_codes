import requests
from bs4 import BeautifulSoup
data = requests.get("http://www.synonym.com/antonyms/cold/")
soup = BeautifulSoup(data.text, "html.parser")
data2 = soup.find('span',{'class':'equals'})
data2.string
data2.contents