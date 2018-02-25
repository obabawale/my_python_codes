from bs4 import BeatifulSoup

html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title"><b>The Dormouse's story</b></p>

		<p class="story">Once upon a time there were three little sisters; and their names were
		<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.</p>
	</body>
</html>"""

soup = BeatifulSoup(html_doc, "html.parser")
print (soup.prettify())

print(soup.title)
print(soup.head)
print(soup.body)
print(soup.body.b)
array = (soup.find_all("a"))
print(array[0])
print(array[1])
print(array[2])
head_tag = soup.head
body_tag = soup.body

print(head_tag.contents)

for i in body_tag.children:
	print(i)

for i in body_tag.descendants:
	print(i)

print(head_tag.string)
print(head_tag.parent)

soup.find_all(id='link2')