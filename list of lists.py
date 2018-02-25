sue = {'name':"Sue Jones", 'age': 35, 'pay': 40000, 'job': "software"}
bob = {'name':"Bob Smith", 'age': 40, 'pay': 50000, 'job': "hardware"}

people = [sue, bob]

if __name__ == '__main__':
     
    print (list(map((lambda x: x['name']), people)))
    
    
    
    