#! /usr/bin/python
my_list = [
	{
		'name': "Olalekan", 
		'age': ['1','','3']
	}, 
	{
		'name': "Olalekan", 
		'age': ['4','7','8']
	}, 
	{
		'name':"Olusola", 
		'age': ['2', '4.0', '5.0']
	}
]

# Another approach to the consolidated trial balance report
cleaned = []
for rec in my_list:
	if cleaned:
		name_list = [x['name'] for x in cleaned]
		if rec['name'] in name_list:
			fetch_rec = [y for y in cleaned if y['name'] == rec['name']]
			fetch_rec = fetch_rec[0]
			mod_fetch_rec_age = [int(x) if x else 0 for x in fetch_rec['age']]
			mod_rec_age = [int(y) if y else 0 for y in rec['age']]
			mod_fetch_rec_age = [str(a) if a else '' for a in [x + y for x, y in zip(mod_fetch_rec_age, mod_rec_age)]]
			fetch_rec['age'] = mod_fetch_rec_age
		else:
			cleaned.append(rec)
	else:
		cleaned.append(rec)
print "Cleaned == ", cleaned