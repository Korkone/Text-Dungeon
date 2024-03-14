Enemy_HP1 = 1
Enemy_HP2 = 1
Enemy_HP3 = 1
Player_HP = 1
Player_Name = "None"
def game_Stop():
    if Player_HP <= 0:
        print("Game Over")
        return False
    else:
        return True

def enemy_dead():
    if Enemy_HP1 <= 0 and Enemy_HP2 <= 0 and Enemy_HP3 <= 0:
        print("Nice job onward to the next Room")
        return False

if __name__ == "__main__":
    ...
