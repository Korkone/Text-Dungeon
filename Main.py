import random
import stuff
#Read the Highscore File to record the Old Highscore
def load_Score():
    global old_Highscore
    f = open("Highscore.txt", "r")
    old_Highscore = f.read()
    f.close()

#Enemy CLasses
class Enemy():
    def __init__(self, Type, Class, HP, Mana, Weakness1, Weakness2, Weakness3, Weakness4, Resistance1, Resistance2,
                 Resistance3):
        self.Type = Type
        self.Class = Class
        self.HP = HP
        self.Mana = Mana
        self.Weakness1 = Weakness1
        self.Weakness2 = Weakness2
        self.Weakness3 = Weakness3
        self.Weakness4 = Weakness4
        self.Resistance1 = Resistance1
        self.Resistance2 = Resistance2
        self.Resistance3 = Resistance3

    def Movement(self, Speed, Style):
        self.Speed = Speed
        self.Style = Style

    def Combat(self, Attack1, Attack2, Ability1, Ability2):
        self.Attack1 = Attack1
        self.Attack2 = Attack2
        self.Ability1 = Ability1
        self.Ability2 = Ability2

#Skeleton Classes
class Skeleton(Enemy):
    def __init__(self, Type, Class, HP, Mana, Weakness1, Weakness2, Weakness3, Weakness4, Resistance1, Resistance2,
                 Resistance3, Vision):
        super().__init__(Type, Class, HP, Mana, Weakness1, Weakness2, Weakness3, Weakness4, Resistance1, Resistance2,
                         Resistance3)
        self.Vision = Vision

class Player_Class():

    def __init__(self, Class, HP, Mana, Weakness1, Weakness2, Resistance1, Resistance2,DodgeChance):
        self.Class = Class
        self.HP = HP
        self.Mana = Mana
        self.Weakness1 = Weakness1
        self.Weakness2 = Weakness2
        self.Resistance1 = Resistance1
        self.Resistance2 = Resistance2
        self.DodgeChance = DodgeChance
    def Combat(self,Attack1, Attack2):
        self.Attack1 = Attack1
        self.Attack2 = Attack2


#Classes for the Player to Choose

Warrior = Player_Class("Warrior", 300, 0, "Range","None", "Blunt", "None", "None")
Rogue = Player_Class("Rogue", 200, 0, "Fire", "None", "Range", "None", "yes")
Mage = Player_Class("Mage", 150, 200, "blunt", "None", "Fire", "Ice", "None")

Class_Choice = "None"
Class_HP = "None"
Class_Mana = "None"
Class_Weakness = "None"
Class_Weakness2 = "None"
Class_Resistance = "None"
Class_Resistance2 = "None"

#List that gets filled with the Players Class attributes

Player_Class_Choice = ["", Class_Choice, Class_HP, Class_Mana, Class_Weakness, Class_Weakness2, Class_Resistance, Class_Resistance2]

#Implemented Skeleton Enemys!

Skeleton_Mage = Skeleton("Skeleton", "Mage", 100, 200, "Holy", "Blunt", "None", "None", "Unholy", "Piercing", "None",
                         "Area")
Skeleton_Mage.Combat("StaffAttack", "None", "FireBall", "IceLance")
Skeleton_Mage.Movement("Slow", "None")

Skeleton_Warrior = Skeleton("Skeleton", "Warrior", 300, 0, "Holy", "Blunt", "None", "None", "Unholy", "Piercing",
                            "None", "Area")
Skeleton_Warrior.Combat("Swort_Attack", "Shild_Bash", "Taunt", "None")
Skeleton_Warrior.Movement("Medium", "Blocking")

Skeleton_Archer = Skeleton("Skeleton", "Archer", 150, 0, "Holy", "Blunt", "None", "None", "Unholy", "Piercing", "None",
                           "Area")
Skeleton_Archer.Combat("Arrow_Shot", "Multishot", "Smoke_Bomb", "None")
Skeleton_Archer.Movement("Fast", "Agile")

# Lootlist "So far just one maybe creat another one.
lootlist = ["", "Healpotion", "Manapotion", "Bandage", "Rusty sword"]

# Enemyobjekts to help creating random encounter.
Enemylist = ("", Skeleton_Mage.Class, Skeleton_Archer.Class, Skeleton_Warrior.Class)
Gegner1 = None
Gegner2 = None
Gegner3 = None
Type1 = None
Type2 = None
Type3 = None
Encounter = None
Score = 4
Player_Class = "none"

#Def thats akts kinda like a starting screen

def start ():
    global old_Highscore
    while True:
        print("Please choose one of the following options! Highscore / Info / Creator / start")
        eingabe = input("")
        if eingabe == "Highscore" or eingabe == "highscore":
            if int(old_Highscore) <= 0:
                print("There is no Highscore jet!")
                print("")
                continue
            else:
                print("The Highscore is " + old_Highscore + " rooms")
                print("")
                continue

        elif eingabe == "Creator" or eingabe == "creator":
            print("This game was created by Pascal Schmid to further learn the basics of Phyton")
            print("")
            continue
        elif eingabe == "Info" or eingabe == "info":
            print("This is a text based simple dungeon crawler. you can enter rooms and destroy random enemys to get loot that helps you getting further into the dungeon!")
            print("")
            continue
        elif eingabe == "start" or eingabe == "Start":
            print("")
            break
        else:
            print("Thats not an Option")
            print("")
            continue



#Def to write the new Highscore into the file !!! If the Score is better !!!
def Bestscore():
    global old_Highscore
    f = open("Highscore.txt", "w")
    if int(old_Highscore) <= Score:
        f.write(str(Score))
    else:
        return None
    f.close()

#Random Encounter Generator "Maybe need to copy this and creat multipal ones to give the Player choices to pick from
def EnemyDifficulty():
    global Gegner1
    global Gegner2
    global Gegner3
    global Type1
    global Type2
    global Type3
    global Encounter
    Encounter = random.randint(1, 10)
    print(Encounter)
    if Encounter <= 4:
        Gegner1 = Enemylist[random.randint(1, 3)]
        Type1 = Skeleton_Mage.Type

    elif Encounter <= 7:
        Gegner1 = Enemylist[random.randint(1, 3)]
        Gegner2 = Enemylist[random.randint(1, 3)]
        Type1 = Skeleton_Mage.Type
        Type2 = Skeleton_Archer.Type
    else:
        Gegner1 = Enemylist[random.randint(1, 3)]
        Gegner2 = Enemylist[random.randint(1, 3)]
        Gegner3 = Enemylist[random.randint(1, 3)]
        Type1 = Skeleton_Mage.Type
        Type2 = Skeleton_Archer.Type
        Type3 = Skeleton_Warrior.Type

    if Encounter <= 4:
        print(Type1, Gegner1)
    elif Encounter <= 7:
        print(Type1, Gegner1)
        print(Type2, Gegner2)
    else:
        print(Type1, Gegner1)
        print(Type2, Gegner2)
        print(Type3, Gegner3)

#Def to give the Player loot after the encounter "Need to aktivate this IF the player aktually wins the encounter
def Loot():
    print("you find a " + lootlist[random.randint(1, 4)])
    lootgold = random.randint(1, 20)
    if lootgold > 1:
        print("you also find " + str(lootgold) + " Goldcoins")
    else:
        print("you also find " + str(lootgold) + " Goldcoin")

#Def to quit the game or stop the game is needet
def breakloop():
    answere = input("Do you wana continue the Dungeon? y/n: ")

    if answere == "n" or answere == "N":
        return False
    else:
        return True


def Kampfverlauf():
    while breakloop() == True:

        EnemyDifficulty()

# This Lets the player Choos his Name
def Player_set_name():
    global Player_Class
    stuff.Player_Name = str(input("Pleas type in your Name: "))
    print("Welcome to the Dungeon " + stuff.Player_Name + " lets get you started with a Class !")
    print("")

#The Player chosses a class here or can get info about the Class also fills out the Player_Class_Choice list with all the classes Attributes
def Player_set_Class():
    global Player_Class
    while True:
        Player_Class = input("you can choos betwenn 3 Classes Warrior/Mage/Rogue if you Wana get some info first Type info: ")
        print("")
        if Player_Class == "Warrior" or Player_Class == "warrior":
            Player_Class_Choice[1] = Warrior.Class
            Player_Class_Choice[2] = Warrior.HP
            Player_Class_Choice[3] = Warrior.Mana
            Player_Class_Choice[4] = Warrior.Weakness1
            Player_Class_Choice[5] = Warrior.Weakness2
            Player_Class_Choice[6] = Warrior.Resistance1
            Player_Class_Choice[7] = Warrior.Resistance2
            print("A Warrior ! good choice, now lets get Started!")
            print("")
            break
        elif Player_Class == "Mage" or Player_Class == "mage":
            Player_Class_Choice[1] = Mage.Class
            Player_Class_Choice[2] = Mage.HP
            Player_Class_Choice[3] = Mage.Mana
            Player_Class_Choice[4] = Mage.Weakness1
            Player_Class_Choice[5] = Mage.Weakness2
            Player_Class_Choice[6] = Mage.Resistance1
            Player_Class_Choice[7] = Mage.Resistance2
            print("A Mage ! good choice, now lets get Started!")
            print("")
            break
        elif Player_Class == "Rogue" or Player_Class == "rogue":
            Player_Class_Choice[1] = Rogue.Class
            Player_Class_Choice[2] = Rogue.HP
            Player_Class_Choice[3] = Rogue.Mana
            Player_Class_Choice[4] = Rogue.Weakness1
            Player_Class_Choice[5] = Rogue.Weakness2
            Player_Class_Choice[6] = Rogue.Resistance1
            Player_Class_Choice[7] = Rogue.Resistance2
            print("A Rogue! good choice, now lets get Started!")
            print("")
            break
        elif Player_Class == "Info" or Player_Class == "info":
            print("Warriors start with " + str(Warrior.HP) + " HP but have 0 Mana, they are Weak to Range Damage but Resistance to Blunt and piercing")
            print("Mages start with "+ str(Mage.HP) + " HP and have "+ str(Mage.Mana) +" Mana, they are Weak to blunt Damage but Resistance to Fire and Ice")
            print("Rogues start with " + str(Rogue.HP) + " HP and have " + str(Rogue.Mana) + " Mana, they are Weak to Fire Damage but Resistance to Range and have a low dodge chance!")
            print("")
            continue
        else:
            print("That´s not an Option pleas try again")
            continue


if __name__ == "__main__":
    load_Score()
    start()
    Player_set_name()
    Player_set_Class()
    Kampfverlauf()
    stuff.Fight_Stop()
    Bestscore()


else:
    ...