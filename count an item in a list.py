def count(x, y):
    if not type(x) == list:
        raise TypeError("x should be a list")
    elif y not in x:
        return 0
    else:
        b = {}
        count = 0
        for i in range(len(x)):
            if x[i] == y:
                count += 1
                b[y] = count
        return count
    
print(count([1, 2, 3, 4, 2, 3, 2, 2, 1], 3))
            
        