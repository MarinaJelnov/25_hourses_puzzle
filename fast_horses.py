#this code runs the simulation of solution of popular work interview task:
#There is 25 houses and you must determine, 3 the fastest of them. You can run them 7 times only. You can run 5 of them one time/
#The main principle of our solution is: the horse has dropped then, and only then, when it is proven that ther is tree who are faster from.
import random
#bronze_horse_club=[]
#silver_horse_club=[]
golden_horse_club=[]
platinum_horse_club=[]
#creating list of 25 houses, and spliting them for 5 groups:
list_horse=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
first_group_of_horses=list_horse[0:5]
second_group_of_horses=list_horse[5:10]
third_group_of_horses=list_horse[10:15]
fourth_group_of_horses=list_horse[15:20]
fifth_group_of_horses=list_horse[20:25]
print('first horse group',first_group_of_horses)
print('second horse group',second_group_of_horses)
print('third horse group',third_group_of_horses)
print('fourth horse group',fourth_group_of_horses)
print('fifth horse group',fifth_group_of_horses)
#The function that has running the group of 5 horses for choising the three fastest of them:
def from_five_to_three(list_x):
    list_xx=[]
    for item in list_x:
     x=random.choice(list_x)
     list_xx.append(x)
    list_xx=list(set(list_x))
    L=len(list_xx)
    if L==3:
     print('Hello World!')
    elif L==4:
     list_xx.pop()
    elif L==5:
     list_xx.pop()
     list_xx.pop()
    elif L<3:
     x = random.choice(list_x)
     list_xx.append(x)
     if L==3:
      pass
    return list_xx
print('Three the best of the evry group:')
list111=list(from_five_to_three(first_group_of_horses))
print(list111)
list222=list(from_five_to_three(second_group_of_horses))
print(list222)
list333=list(from_five_to_three(third_group_of_horses))
print(list333)
list444=list(from_five_to_three(fourth_group_of_horses))
print(list444)
list555=list(from_five_to_three(fifth_group_of_horses))
print(list555)
#create the bronze group of the firsts horses of evry group:
bronze_horse_club=[list111[0],list222[0],list333[0],list444[0],list555[0]]
print('The Bronze Horses Club',bronze_horse_club)
#run this group for determine three the fastest in it, and create the silver club group of them:
silver_horse_club=list(from_five_to_three(bronze_horse_club))
print('The Silver Horses Club',silver_horse_club)
#the first horse of our silver club is now one of the winner. We can build now the gold club of houses, which is
#the group of five horse for running, when we will run the second and the third horse of the group of the hourse,
#who is the fasterst in the silver club,the second horse of the silver group, and the second horse of its previous group,
# and the thirt horse of the silver group. The first horse in the silver club is out of competition now,
#because it's one of the winner obviosly:
golden_horse_club.append(silver_horse_club[1])
golden_horse_club.append(silver_horse_club[2])
if silver_horse_club[0]==list111[0]:
    golden_horse_club.append(list111[1])
    golden_horse_club.append(list111[2])
elif silver_horse_club[0]==list222[0]:
    golden_horse_club.append(list222[1])
    golden_horse_club.append(list222[2])
elif silver_horse_club[0]==list333[0]:
    golden_horse_club.append(list333[1])
    golden_horse_club.append(list333[2])
elif silver_horse_club[0]==list444[0]:
    golden_horse_club.append(list444[1])
    golden_horse_club.append(list444[2])
elif silver_horse_club[0]==list555[0]:
    golden_horse_club.append(list555[1])
    golden_horse_club.append(list555[2])
if silver_horse_club[1]==list111[0]:
    golden_horse_club.append(list111[1])
elif silver_horse_club[1]==list222[0]:
    golden_horse_club.append(list222[1])
elif silver_horse_club[1]==list333[0]:
    golden_horse_club.append(list333[1])
elif silver_horse_club[1]==list444[0]:
    golden_horse_club.append(list444[1])
elif silver_horse_club[1]==list555[0]:
    golden_horse_club.append(list555[1])
print('The Golden Horse Club:',golden_horse_club)
#We are running our gold club of the horses and adding the two fastest of them, wth thouse the first in silver club,
#to the Platinum Club, which is the winner club of 3 the fastest horses from the 25:
platinum_horse_club=list((from_five_to_three(golden_horse_club)))
platinum_horse_club.pop()
platinum_horse_club.insert(0, silver_horse_club[0])
print('The Platinum Winner Club:',platinum_horse_club)
















