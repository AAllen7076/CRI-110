def main():
  menu()

def menu():
    repeat = 1
    choice = 0
    scorelist = []
    while repeat != 0:
        print()
        print('----MENU----')
        print('1. Create Score List')
        print('2. Display Results')
        print('3. Exit')
        print('------------')


        choice = input("Enter a choice 1 or 2 or 3: ")
        if choice == '1':
           scorelist = createlist()
        elif choice == '2':
            if len(scorelist) == 0:
                print('List not created!')
            else:
                calcScores(scorelist)
        elif choice == '3':
            repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1
            
    print('Program Terminated!')
def calcScores(lis):
    lowNum = min(lis)
    lis.remove(lowNum)
    liMod = lis
    liAvg = sum(lis) / len(lis)
    if (liAvg >= 90):
        grade = 'A'
    elif (liAvg < 90 and liAvg >= 80):
        grade = 'B'
    elif (liAvg < 80 and liAvg >= 70):
        grade = 'C'
    elif (liAvg < 70 and liAvg >= 60):
        grade = 'D'
    elif (liAvg < 60 and liAvg >= 0):
        grade = 'F'
    values = [lowNum, liMod, liAvg, grade]
    printList(values)

  
def getScores(mList):
    liScores = []
    n = 0
    while n < mList:
        score = int(input('Enter score:'))
        if (score > 100 or score < 0):
          print ('Invalid Entry')
          print()
          n = n
        else: 
          liScores.append(score)
          n += 1
    return liScores
    
      
def createlist():
  index = int(input('Enter in the number of scores:'))
  countscores = getScores(index)
  return countscores

def printList(f_result):
    #prints values
    print('Lowest score:',f_result[0])
    print('List of scores (lowest omitted):',f_result[1])
    print('Average:',f_result[2])
    print('Letter Grade:',f_result[3])


main()