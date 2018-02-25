class pet:
	number_of_legs = 0

	def sleep(self):
		print ('zzz')

	def count_legs(self):
		print ('I have %s legs' % self.number_of_legs)

doug = pet()
doug.number_of_legs = 4

nemo = pet()
nemo.number_of_legs = 0

doug.sleep()
doug.count_legs()

nemo.sleep()
nemo.count_legs()


