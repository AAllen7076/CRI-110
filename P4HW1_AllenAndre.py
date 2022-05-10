#CTI-110
#P4HW1_ScoreList
#AndreAllen
#03/27/2022
print("Enter the amount of scores you want to enter")
ascores = int(input())
qi = int(1)
verifiedlist = []
while ascores > 0:
    print('Enter score #',qi,':')
    answers = float(input())
    qi += 1
    ascores -= 1
    verifiedlist.append(answers)
    if answers > 100 or answers < 0:
        print('Invalid Score Entered !!!!')
        print('Score should be between 0 and 100')
        print('Enter score #',qi - 1 ,' again:')
        answer = float(input())
        continue
print('Lowest Score : ',min(verifiedlist))
verifiedlist.remove(min(verifiedlist))
avg = sum(verifiedlist)/len(verifiedlist)
print('Modified List; ',verifiedlist)
if(avg >= 90):
 print('Grade    : A')
if(avg >= 80) and (avg <= 89):
 print('Grade    : B')
if(avg >= 70) and (avg <= 79):
 print('Grade    : C')
if(avg >= 60) and (avg <= 69):
 print('Grade    : D')
if(avg <= 59):
 print('Grade    : F')
print('Scores Average: ',avg)




