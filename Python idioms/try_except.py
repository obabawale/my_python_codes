d = {'x': '5'}
try:
    value = int(d['x'])
    
except (KeyError, TypeError, ValueError):
    value = None
    
print(d)