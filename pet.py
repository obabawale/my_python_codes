class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # you can run super method
        
def Main():
    thePet = Pet('Pet', 1)
    jess = Cat("jess", 3)
    
    print("is jess a cat?" + str(isinstance(jess,Cat)))
    print("is jess a pet?" + str(isinstance(jess,Pet)))
    print("is thePet a Cat?" + str(isinstance(thePet, Cat)))
    print("is thePet a Pet?" + str(isinstance(thePet,Pet)))
    
    print(jess.name)

if __name__  == "__main__":
    Main()

