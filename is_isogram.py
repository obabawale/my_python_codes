# this function determines if a number is an isogram or not
def is_isogram(word):
  
  # check if the string is empty or not
  if isinstance(word, str):
    
    # determine if the word is an empty string or not    
    word2 = set(word.lower()) # convert all letters to lowercase
    
    #check if the string is not empty
    if word:
      if len(word) == len(word2): # tests for isogram
        return word, True
      else:
        return word, False
    else:
      return (word, False)
  else:
    raise TypeError('Argument should be a string')