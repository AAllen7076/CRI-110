#Andre Allen Jr
#04/19/2022
#CTI-110
#Math Quiz 


def menu():
   print('Welcome to Math Quiz')
   print()
   print()
   print ('MAIN MENU')
   print ('--------------------')
   print ('1. Adding Random Numbers')
   print ('2. Subtracting Random Numbers')
   print ('3. Exit')
   print()
   
   choice = int(input('Please chooose from these 3 menu options:'))
   if choice == 1:
       agetRandom()
   if choice == 2:
       sgetRandom()
   else:
       stop(choice)
       
 
# Adds and validates Random numbers
import random
def agetRandom():
        ng = 2
        n1 = random.randint(0, 999)
        n2 = random.randrange(0, 999)
        add_ans = n1 + n2
        print(n1)
        print('+',n2)
        guess = int(input('Whats your guess?  '))
        while (ng != 1):
         if (guess > add_ans):
              guess = int (input('Incorrect, guess is too high. Try Again  '))
              continue
              
              
         elif (guess < add_ans):    
              guess = int (input('Incorrect, guess is too low. Try Again  '))
              continue
              

         else: 
           print ("Congradulations!!! you're correct")
           print()
           menu()
# Subtracts and validates Random numbers
def sgetRandom():
      ng = 5
      n1 = random.randint(0, 500)
      n2 = random.randrange(0, 500)
      sub_ans = n1 - n2
      print(n1)
      print('-',n2)
      print()
      guess = int(input('Whats your guess?  '))
      while (ng != 1):
        if (guess > sub_ans):
             guess = int (input('Incorrect, guess is too high. Try Again  '))
             continue
        elif (guess < sub_ans):       
             guess = int (input('Incorrect, guess is too low. Try Again  '))
             continue

        else: 
          print ("Congradulations!!! you're correct")
          print()
          menu()
# Quits Program/ Invalid Entry
def stop(answer):
      if (answer < 3):
        print('Invalid Entry Try Again')
        print()
        menu()
      else:
        print('Bye...')
        print('Thank you for playing!')
        quit()
    
menu()


     
