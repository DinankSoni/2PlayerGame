#task 1 (mini game with use of python external and internal library )
def attackchose(atck):
    
    print("========")
    print(atck,"chose your attack")
    print(" ")

    print("1) normal attck")
    print("2) special attck")
    print("3) recover hp")
    print(" ")

    a0 = int(input("enetr your attack"))

    return a0

import random
import matplotlib.pyplot as plt


p1 = input("enter your name")
print(" ")
p2 = input("enter your name")
print(" ")

p1hp = 100
p2hp = 100
p1dmg = [0]
p2dmg = [0]
hpp1 = [100]
hpp2 = [100]

while p1hp > 0 and p2hp > 0:
#player1 attack
    a0r = attackchose(p1)

    if a0r == 1:

        p2hp -= 10
        print("your damage is",10)
        print(p2,"hp is",p2hp)
        hpp2.append(p2hp)
        p1dmg.append(10)

    
    elif a0r == 2:

        damage1 = random.randint(0,35)
        p2hp -= damage1
        print("your damage is",damage1)
        print(p2,"hp is",p2hp)
        hpp2.append(p2hp)
        p1dmg.append(damage1)


    elif a0r == 3:

        hp1 = random.randint(15,30)
        p1hp += hp1
        print("your recover hp is",hp1)
        print(p1,"hp is",p1hp)
        hpp1.append(p1hp)
        p1dmg.append(0)

    else:
        print("lost attack")

    if p2hp <= 0:
        print(p1,"is win the game")
        break
        

#player 2 attck
    a1r = attackchose(p2)
    
    if a1r == 1:

        p1hp -= 10
        print("your damage is",10)
        print(p1,"hp is",p1hp)
        hpp1.append(p1hp)
        p2dmg.append(10)

    
    elif a1r == 2:

        damage2 = random.randint(0,35)
        p1hp -= damage2
        print("your damage is",damage2)
        print(p1,"hp is",p1hp)
        hpp1.append(p1hp)
        p2dmg.append(damage2)

    elif a1r == 3:

        hp2 = random.randint(15,30)
        p2hp += hp2
        print("your recover hp is",hp2)
        print(p2,"hp is",p2hp)
        hpp2.append(p2hp)
        p2dmg.append(0)

    else:
        print("lost attack")

    if p1hp <= 0:
        print(p2,"is win the game")
        break
        
plt.title("Players health")
plt.plot(hpp1,label='player1')
plt.plot(hpp2,label='player2')
plt.ylabel('Health')
plt.xlabel('Attempt')
plt.legend()
plt.show()
plt.title("Damage by player")
plt.plot(p1dmg,label='player1')
plt.plot(p2dmg,label='player2')
plt.ylabel('Damage')
plt.xlabel('Attempt')
plt.legend()
plt.show()