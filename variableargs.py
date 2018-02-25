def average(*args):
    sum = 0
    for num in args:
        sum += num
    average = sum/len(args)
    return average

