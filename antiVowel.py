def anti_vowel(text):
    new = ''
    for letter in text:
        if letter in 'aeiouAEIOU':
            continue
        new += letter
    return new
    print (new)