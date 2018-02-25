class Staff(object):
    name = "Adeola adebayo Sunday"
    
    def returnSplittedName(self):
        first, last, sur = self.name.split(' ')
        print("First Name " + first + " Lastname " + last + " Surname " + sur)
        
me = Staff()
me.returnSplittedName()