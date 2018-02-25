class Partner:
	_name = 'Ademolu Okuneye'
	_columns = {
	'age' : 24,
	'dateofBirth' : 1989,
	'gender' : 'male',
	}

	def returnID(self):
		if self._name:
			return "The person is " + self._columns['gender'] + " his name is " + self._name + ", and his age is %s ." + \
			" He was born in the year %i therefore he is %s years old"

if "__name__" == "__main__":
	vic = Partner()
	print(vic.returnID())