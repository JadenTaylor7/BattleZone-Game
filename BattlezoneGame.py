import time

class Archer():

    def __init__(self, health = 25, range = 3, damage = 5):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "archer"
        print("Archer Created! Stats:  Health: {}    Range: {}    Damage: {}".format(self.health,range,damage))

    def attack(self):
        print("Archer did {} damage to opponent.".format(self.damage))
        return self.damage

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Archer was hit. -{} hp.     Archer health: {}.".format(impact, self.health))
        else:
            pass


class Squire():

    def __init__(self, health = 35, range = 1, damage = 8):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "squire"
        print("Squire Created! Stats:  Health: {}    Range: {}    Damage: {}".format(self.health,range,damage))

    def attack(self):
        print("Squire did {} damage to opponent.".format(self.damage))
        return self.damage

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Squire was hit. -{} hp.     Squire Health: {}.".format(impact, self.health))
        else:
            pass


class Mage():

    def __init__(self, health = 20, range = 3, damage = 6, heal = 4):
        self.health = health
        self.range = range
        self.damage = damage
        self.name = "Mage"
        self.recharging = True
        self.heal = heal
        print("Mage Created! Stats:  Health: {}    Range: {}    Damage: {}   Healing: {}".format(self.health,range,damage,heal))

    def attack(self):
        if self.recharging == True:
            print("Mage did {} damage to opponent.".format(self.damage))
            self.recharging = False
            return self.damage
        else:
            self.health += self.heal
            print("Mage healed {} life.          Mage Health: {}.".format(self.heal, self.health))
            self.recharging = True
            print("Mage did {} damage to opponent.".format(self.damage))
            return self.damage
        

    def hurt(self, impact):
        self.health -= impact
        if impact > 0:
            print("Mage was hit. -{} hp.         Mage Health: {}.".format(impact, self.health))
        else:
            pass


def battle(troop1, troop2, begin = True):
        if begin == True:
            if troop1.range == 1 and troop2.range == 1:
                pass
            elif troop1.range == 1:
                troop1.hurt(troop2.attack())
                troop1.hurt(troop2.attack())
                time.sleep(2)
            elif troop2.range == 1:
                troop2.hurt(troop1.attack())
                troop2.hurt(troop1.attack())
                time.sleep(2)
            else:
                pass
        

        if troop1.health <= 0 and troop2.health <= 0:
            print("Both {} and {} have fallen.".format(troop1.name, troop2.name))
            time.sleep(2)
        elif troop2.health <= 0:
            print("{} has fallen.".format(troop2.name))
            time.sleep(2)
        elif troop1.health <= 0:
            print("{} has fallen.".format(troop1.name))
            time.sleep(2)
        else:
            print("\n")
            troop1.hurt(troop2.attack())
            time.sleep(1.5)
            troop2.hurt(troop1.attack())
            time.sleep(2)
            battle(troop1, troop2, False)


def multiArmyBattle(list1, list2):
    if not list1 and not list2:
        print("Both teams have been defeated.")
        return True
    elif not list1:
        print("Red team defeated. Blue team wins!")
        return True
    elif not list2:
        print("Blue team defeated. Red team wins!")
        return True
    else:
        pass
    
    print("\n\nTeam Red list:") #displays after troop has fallen
    for i in listRed:
        print(i.name, end = ", ")
    print("\n")
    print("\nTeam Blue list")
    for i in listBlue:
        print(i.name, end = ", ")
    print("\n")
    time.sleep(4)
    print("\n")
    battle(list1[0],list2[0])
    if list1[0].health <= 0 and list2[0].health <= 0:
        list1.pop(0)
        list2.pop(0)
        multiArmyBattle(list1, list2)
    elif list1[0].health <= 0:
        list1.pop(0)
        multiArmyBattle(list1, list2)
    elif list2[0].health <= 0:
        list2.pop(0)
        multiArmyBattle(list1, list2)


#game setup here
listRed = []
listBlue = []
listRed.clear()
listBlue.clear()
dummyA = Archer()
dummyS = Squire()
dummyM = Mage()
listAvailable = ["A","a","S","s","M","m"]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def chooseCharacters(size):
    global listRed
    global listBlue
    tempRed = []
    tempBlue = []
    size = int(size)
    print(type(size))
    print("\n\n\n\n\n      Team Red's turn!\n\n")
    for i in range(0,size,1):
        print("Team Red, pick character {}:".format(i+1))
        print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
        print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
        print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
        z = input("(press A, S, or M, then enter)")
        while z not in listAvailable:
            print("\nPlease select a valid input")
            print("Team Red, pick character {}:".format(i+1))
            print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
            print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
            print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
            z = input("(press A, S, or M, then enter)")
        else:
            print("Thank you\n")
            z = z.lower()
            tempRed.append(z)
    print("\n\n\n\n\n      Team Blue's turn!\n\n")
    for i in range(0,size,1):
        print("Team Blue, pick character {}:".format(i+1))
        print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
        print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
        print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
        z = input("(press A, S, or M, then enter)")
        while z not in listAvailable:
            print("\nPlease select a valid input")
            print("Team Blue, pick character {}:".format(i+1))
            print("(press A) Archer:  Health: {}    Range: {}    Damage: {}".format(dummyA.health, dummyA.range, dummyA.damage))
            print("(press S) Squire:  Health: {}    Range: {}    Damage: {}".format(dummyS.health, dummyS.range, dummyS.damage))
            print("(press M) Mage:    Health: {}    Range: {}    Damage: {}   Healing: {}".format(dummyM.health, dummyM.range, dummyM.damage, dummyM.heal))
            z = input("(press A, S, or M, then enter)")
        else:
            print("Thank you\n")
            z = z.lower()
            tempBlue.append(z)
           

    
    for i in tempRed: #building armies
        if i == "a":
            i = Archer() #FIXME should convert from string to class Archer
            troop = Archer()
            listRed.append(troop)
        elif i == "s":
            i = Squire()
            troop = Squire()
            listRed.append(troop)
        elif i == "m":
            i = Mage()
            troop = Mage()
            listRed.append(troop)
        else:
            print("something went wrong. Debug Building armies")
    
    for i in tempBlue: #building armies
        if i == "a":
            i = Archer()
            troop = Archer()
            listBlue.append(troop)
        elif i == "s":
            i = Squire()
            troop = Squire()
            listBlue.append(troop)
        elif i == "m":
            i = Mage()
            troop = Mage()
            listBlue.append(troop)
        else:
            print("something went wrong. Debug Building armies")
        print(i.name)

    print("\nTeams are chosen")
    print("\n")
    print("Game will start in 5")
    time.sleep(1)
    print("Game will start in 4")
    time.sleep(1)
    print("Game will start in 3")
    time.sleep(1)
    print("Game will start in 2")
    time.sleep(1)
    print("Game will start in 1")
    time.sleep(1)


print("Welcome to the battlezone, where two armies battle against each other.")
print("Characters of each army will battle one at a time.")
input("(press enter to continue)")
print("\n\n\n")
battleSize = input("How large should each army be? (integer from 1-10)")
while not battleSize.isdigit():
    print("Invalid response. Must be an integer.")
    battleSize = input("How large should each army be?")
chooseCharacters(battleSize)
multiArmyBattle(listRed, listBlue)






    

