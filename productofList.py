"""
Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

    Don't worry about the list being empty.
    Your function should return an integer.

You can use a loop to go through the elements of the list.

It'll probably be useful to use the *= operator.

Be careful not to start your total at 0, as this would make the overall result of the multiplication equal to 0! (Anything multiplied by zero equals zero.)

"""

def product(x):
    if not type(x) == list:
        raise TypeError("x should be a list")
    product = 1
    for i in x:
        product *= i
    return product
    
print(product([2,3,4]))
        
        