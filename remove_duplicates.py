def remove_duplicates(string):
    new_string = ""
    count = 0
    if string == string.lower() and string.isalpha():
        for i in string:
            if i not in new_string:
                new_string += i
            else:
                count += 1
        return (''.join(sorted(new_string)), count)
    else:
        print("invalid input")
                