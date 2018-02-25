"""

Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

    Don't remove every occurrence, since you need to keep a single occurrence of a n

    umber.
    The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
    Do not modify the list you take as input! Instead, return a new list.
"""

def remove_duplicates(x):
    if not type(x) == list:
            raise TypeError("x should be a list")
    else:
        b = []
        for i in range(len(x)):
                for y in x:
                    if y in b:
                        continue
                    b.append(y)
        return b
        
print(remove_duplicates([1, 2, 3, 4, 2, 3, 2, 2, 1]))    
