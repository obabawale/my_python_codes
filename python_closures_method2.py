def make_multiplier_of():
    return [lambda x : x * 3] 

for multiplier in make_multiplier_of():
    print(multiplier(5))