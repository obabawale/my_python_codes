grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  sum = 0
  for item in scores:
    sum += item
  return sum

def grades_average(grades_input):  
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
    
print(grades_average(grades))