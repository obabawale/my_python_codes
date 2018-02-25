a = [1, 2, 3, 4, 2, 3, 2, 2, 1]

b = {}

for i in range(len(a)):
    count = 0
    for k in a:
        if a[i] == k:
            count += 1
            b[k] = count
print(b)
            
        