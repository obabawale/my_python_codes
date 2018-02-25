# This code performs some sorting on a list of tuples and 
# a list of dictionaries using certain keys

# (name, score, age,)

record = [('Nik', 9, 18),
	('Rob', 8, 19), 
	('Sam', 8, 18), 
	('Harry', 6, 20),]

from operator import itemgetter

# this can be used to get the result k = itemgetter(1)

# print (*map(k, record))
# print (sorted(record))

print(sorted(record, key=itemgetter(1)))

"""
Now for a list of dcitionaries
"""
record2 = [{'name': 'Nik', 'score':9, 'age': 18},
           {'name':'Rob', 'score':8, 'age':19},
           {'name':'Sam', 'score':8, 'age':18},
            {'name':'Harry', 'score':6, 'age':20},]

print(sorted(record2, key=itemgetter('name')))