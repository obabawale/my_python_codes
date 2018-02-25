class Pet:
    number_of_legs = 0
    
    def sleep(self):
        print "zzz"
        
    def count_number_of_legs(self):
        print "I have %s legs" % self.number_of_legs
        
doug = Pet()
doug.number_of_legs = 4
doug.count_number_of_legs()
    
nemo = Pet()
nemo.number_of_legs = 0
nemo.count_number_of_legs()