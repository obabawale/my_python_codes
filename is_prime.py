def is_prime(x):
    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    elif x > 2:        
        for n in range(2, x):
            if x % n == 0:
                return False
            break
        return True
    else:
        return False
    