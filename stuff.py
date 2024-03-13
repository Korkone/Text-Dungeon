Enemy_HP1 = 0
Enemy_HP2 = 0
Enemy_HP3 = 1
Player_HP = 0
Player_Name = "Peter"
def Fight_Stop():
    if Enemy_HP1 <= 0 and Enemy_HP2 <= 0 and Enemy_HP3 <= 0:
        print("Nice job onward to the next Dungeon")
    elif Player_HP <=0:
        print("Game Over")
        print("Thanks for Playing " + Player_Name + " maybe you can get further next try.")
    else:
        return True

if __name__ == "__main__":
    ...