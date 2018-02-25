#
#foo1 = [2, 18, 9, 22, 17, 24, 8, 12, 27]
#foo2 = {'a':2, 'b':18, 'c': 9}
#print(list(filter(lambda x: x % 3 == 0, foo)))

#loop = [x for x in range(0,12) if x % 2 == 0]

#print(loop)

#print(list(filter(lambda x : x % 2 == 0, range(0,12))))

#print(list(filter(lambda x : x % 2 == 0, range(0, 12))))

#print(list(range(0, 12)).mapped(lambda x : x % 2 == 0))

foo1 = {'name': 'Axelor', 'age': 20, 'sex': ' Male'}
foo2 = {'name': 'Dolly', 'age': 25, 'sex': ' Female'}
foo3 = {'name': 'Andela', 'age': 30, 'sex': ' Female'}
foo4 = {'name': 'Endocryne', 'age': 45, 'sex': ' Male'}
foo = [foo1, foo2, foo3, foo4]

def returnitem(x):
    for item in x:
        print (item['name'])

returnitem(foo)
result = list(map(lambda item: item['name'], foo))
print(result)