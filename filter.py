squares = [num*num for num in range(1,11)]
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))