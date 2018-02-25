def addNum(num1, num2):
    try:
        diff = int(num1) - int(num2)
    except (ValueError, NameError, TypeError) as e:
        print ("Check the value of inputed numbers")
    else:
        print (diff)
    