import math
pizzas = int()
print('Enter number of students that will be eating pizza')
students = int(input())
print('Enter number of students that will sharing each  pizza (1.5, 2, 3):')
shared = float(input())
if shared == 1.5:
  pizzas = math.ceil((students / 1.5))
  price = (pizzas * 5) 
  tax = (price * 0.06) 
  price = price + tax
  print ('Number of students:',students)
  print ('Pizzas needed:',pizzas)
  print ("Price is ${:.2f}".format(price))
elif shared == 2:
  pizzas = math.ceil((students / 2))
  price = (pizzas * 5) 
  tax = (price * 0.06) 
  price = price + tax
  print ('Number of students:',students)
  print ('Pizzas needed:',pizzas)
  print ("Price is ${:.2f}".format(price))
elif shared == 3:
  pizzas = math.ceil((students / 3))
  price = (pizzas * 5) 
  tax = (price * 0.06) 
  price = price + tax
  print ('Number of students:',students)
  print ('Pizzas needed:',pizzas)
  print ("Price is ${:.2f}".format(price))
else:
  print('Invalid Entry!!!!')
  print('Should have entered: 1.5, 2, or 3')
  print('Run the program again')
#import math
# 