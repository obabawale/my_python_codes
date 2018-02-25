def median(x):
    if not type(x) == list:
        raise TypeError("x should be a list")
    
    if len(x) == 1:
        return x[0]
    
    orderedList = sorted(x)
    if len(orderedList) % 2 != 0:      
        medPosition = (len(orderedList) // 2)
        return orderedList[medPosition]
    
    else:
        medpos1 = ((len(orderedList))//2)
        medpos2 = medpos1 - 1
        sumMed = (orderedList[medpos1] + orderedList[medpos2])
        median = sumMed / 2.0
        return median

print(median([4, 5, 5, 4,4]))