word = 'Almighty'
# word = 'Adeolu Adepegba'
new_word = word.lower()
word_dict = dict((letter, new_word.count(letter)) for letter in set(new_word))
word_list = list(new_word.count(letter) for letter in set(new_word))
print (str(word_dict) + "\n")
print (str(word_list) + "\n")
max_word_list = max(word_list)
print (str(max_word_list) + "\n")
if max_word_list > 1:
    print ("The word "+ word + " is not an isogram ")
else:
	print("The word " + word + " is an isogram ")