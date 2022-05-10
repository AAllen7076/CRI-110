# CTI-110
# P2HW2 - Score Avg
# Andre Allen Jr
# 02/26/2022

#Display enter score and receive input
print('Enter score 1: ')
score1 = float (input())
print('Enter score 2: ')
score2 = float (input())
print('Enter score 3: ')
score3 = float (input())
print('Enter score 4: ')
score4 = float (input())
print('Enter score 5: ')
score5 = float (input())
print('Enter score 6: ')
score6 = float (input())
print('Enter score 7: ')
score7 = float (input())
Scores = [score1, score2, score3, score4, score5, score6, score7]
#Removes lowest score from list
Scores.remove(min(Scores))
#Calculates average of list
average = (sum(Scores) / 6)
#Prints Results
print('-------Results--------')
print('Lowest Score :', min(Scores))
print('Modified List :',Scores)
print ('Scores Average: {0:.2f}'.format(average))
print('-------------')

#Display Enter Score 1
#Input score1
#Display Enter Score 2
#Input score2
#Display Enter Score 3
#Input score3
#Display Enter Score 4
#Input score4
#Display Enter Score 5
#Input score5
#Display Enter Score 6
#Input score6
#Display Enter Score 7
#Input score7
#Set Scores = [score1, score2, score3, score4, score5, score6, score7]
#Remove min(Scores)
#Set average = Scores / 6
#Display Lowest Score: ,min(Scores)
#Display Modified List: ,Scores
#Display Scores Average: ,average