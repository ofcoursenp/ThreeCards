
import random
from secrets import choice

spade = ["S14","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]
heart = ["H14","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13"]
clubs = ["C14","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13"]
diamond = ["D14","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13"]





user1Trial = False
user2Trial = False
user1Jut = False
user2Jut = False
user2Run = False
user1Run = False
user1colorlRun = False
user2colorlRun = False
user2Color = False
user1Color = False
highUser2Card = False
highUser1Card = False


def randomcard_TeenPatti_generator():
    global spade
    global heart
    global clubs
    global diamond
    random_kitti_UserOne = []
    random_kitti_UserTwo = []
    choice = ""
    ru1 = 1
    while ru1 <= 3:
        rc = random.randint(1,4)
        if choice == "":
            if rc == 1:
                choice = random.choice(spade)
            if rc == 2:
                choice = random.choice(heart)
            if rc == 3:
                choice = random.choice(clubs)
            if rc == 4:
                choice = random.choice(diamond)    
        if choice not in random_kitti_UserOne:
            random_kitti_UserOne.append(choice)
            ru1+=1
            choice = ""
        else:
            choice = ""
            continue

    choice = ""
    ru2 = 1
    while ru2 <= 3:
        rc = random.randint(1,4)
        if choice == "":
            if rc == 1:
                choice = random.choice(spade)
            if rc == 2:
                choice = random.choice(heart)
            if rc == 3:
                choice = random.choice(clubs)
            if rc == 4:
                choice = random.choice(diamond)    
        if choice not in random_kitti_UserTwo:
            random_kitti_UserTwo.append(choice)
            ru2 +=1
            choice = ""
        else:
            choice = ""
            continue

    l1 = random_kitti_UserOne
    l2 = random_kitti_UserTwo
    return l1,l2
    

l1,l2 = randomcard_TeenPatti_generator()




print(f"---> 1st person {l1}")
print(f"---> 2nd person {l2}")

Doing = True


#This category for user 1

# Checks if the player has got trial
if int(l1[0][1::]) == int(l1[1][1::]) and int(l1[1][1::]) == int(l1[2][1::]) and int(l1[0][1::]) == int(l1[2][1::]):
    user1Trial = True

# Checks if the player has got run
elif int(l1[0][1::])+1 == int(l1[1][1::]) and int(l1[1][1::])+1 == int(l1[2][1::]):
    user1Run = True

    # Checks if the player has got run + color
    if l1[0][0] == l1[1][0] and l1[2][0] == l1[0][0]:
        user1colorlRun = True
        user1Run = False

# Checks for color in user 1
elif l1[0][0] == l1[1][0] and l1[2][0] == l1[0][0]:
    user1Color = True

# checks for 2 cards similar in user 1
elif l1[0][1::] == l1[1][1::] or l1[1][1::] == l1[2][1::] or l1[2][1::] == l1[1][1::] or l1[0][1::] == l1[2][1::]:
    user1Jut = True

else:
    highUser1Card = True
    randomUser1Order = [int(l1[0][1::]),int(l1[1][1::]),int(l1[2][1::])]
    randomUser1Order.sort()
    highestCardUser1 = int(randomUser1Order[-1])




# This category for User 2
if int(l2[0][1::]) == int(l2[1][1::]) and int(l2[1][1::]) == int(l2[2][1::]) and int(l2[0][1::]) == int(l2[2][1::]):
    user2Trial = True

#Checks for run for user 2
elif int(l2[0][1::])+1 == int(l2[1][1::]) and int(l2[1][1::])+1 == int(l2[2][1::]):
    user2Run = True

    # Checks for color run in user 2
    if l2[0][0] == l2[1][0] and l2[2][0] == l2[0][0]:
        user2colorlRun = True
        user2Run = False

# Checks for color in user 2
elif l2[0][0] == l2[1][0] and l2[2][0] == l2[0][0]:
    user2Color = True

# checks for 2 cards similar
elif l2[0][1::] == l2[1][1::] or l2[1][1::] == l2[2][1::] or l2[2][1::] == l2[1][1::] or l2[0][1::] == l2[2][1::]:
    user2Jut = True

else:
    highUser2Card = True
    randomUser2Order = [int(l2[0][1::]),int(l2[1][1::]),int(l2[2][1::])]
    randomUser2Order.sort()
    highestCardUser2 = int(randomUser2Order[-1])




if user1Trial == True and user2Trial != True:
    print("user 1 won with trial")

if user1Trial != True and user2Trial == True:
    print("user 2 won with trial")

if user1colorlRun != True and user2colorlRun == True:
    print("user 2 won with Color run")

if user1colorlRun == True and user2colorlRun != True:
    print("user 1 won with Color run")

if user1Run != True and user2Run == True:
    print("user 2 won with Run")

if user1Run == True and user2Run != True:
    print("user 1 won with Run")

if user1Color == True and user2Color != True:
    print("user 1 won with Color")

if user1Color != True and user2Color == True:
    print("user 2 won with Color")

if user1Jut == True and user2Jut != True:
    print("User 1 won with jut")

if user1Jut != True and user2Jut == True:
    print("User 2 won with jut")

if highUser1Card == True and highUser2Card == True:
    if highestCardUser2 > highestCardUser1:
        print("User 2 won the game woohoo")
    if highestCardUser2 < highestCardUser1:
        print("User 1 won the game wohoo")
    
    if highestCardUser2 == highestCardUser1:
        if int(randomUser1Order[1]) > int(randomUser2Order[1]):
            print("User 1 won the game ")

        if int(randomUser1Order[1]) < int(randomUser2Order[1]):
            print("User 2 won the game ")

        if int(randomUser1Order[1]) == int(randomUser2Order[1]):
            if int(randomUser1Order[0]) > int(randomUser2Order[1]):
                print("User 1 won")
            if int(randomUser1Order[0]) < int(randomUser2Order[0]):
                print("User 2 won")

            else:
                print("Its a draw")



















