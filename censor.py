
def censor(text, word):
 myList = text.split() 
 for i,v in enumerate(myList):
  if v == word:
   myList.pop(i)
   myList.insert(i, "*" * len(word))
 newText = ' '.join(myList)
 return (newText)