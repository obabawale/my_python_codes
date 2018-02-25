"""
Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, 
and returns the result. For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
"""

def purify(x):
    if not type(x) == list:
        raise TypeError("x should be a list")
    else:
        b = []        
        for i in x:
            if i % 2 == 0:
                b.append(i)
            continue
        return b
    
print(purify([1, 2, 3, 4, 2, 3, 2, 2, 1]))