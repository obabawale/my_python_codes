def reverse(text):
    outputStr = ''
    a = input("Enter String: ")
    for i in range(len(a), 0, -1):
        outputStr += a[i-1]
    return outputStr

    