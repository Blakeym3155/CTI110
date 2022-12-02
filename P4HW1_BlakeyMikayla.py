# CTI-110
# P4HW1 - Score List
# Mikayla Blakey
# 11/22/22
#
#--------------------Pseudocode--------------------------------
#

num_scores = int(input("How many scores do you want to enter:"))
print(" ")
scores = []
for i in range(num_scores):
    
    score = float(input(f'Enter Score #{i + 1}: '))
    while score < 0 or score > 100:
        print(" ")
        print("INVALID SCORE entered!!!")
        print("Score should be between 0 and 100")
        score = float(input(f'Enter score #{i + 1} again:'))
    scores.append(score)          
new_score = scores
print(" ")
print(" ")
    
print('---------------------Results------------------------')
print('Lowest Grade :', min(scores))
scores.remove(min(scores))
print('Modified List:', scores )
score_average = sum(scores) / len(scores)
print('Score Average:', score_average)
if score_average >= 90:
    print("Grade        : A")
elif score_average >= 80:
    print("Grade        : B")
elif score_average >= 70:
    print("Grade        : C")
elif score_average >= 60:
    print("Grade        : D")
elif score_average >= 50:
    print("Grade        : E")
else:
    print("Grade        : F")
print('---------------------------------------------------')
    
