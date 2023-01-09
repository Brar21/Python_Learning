#Random.randint() to print radom number every time
#you have to import random
import random
def snakewatergun(computer,player):
    if computer == player:
                return None
    elif computer == 's':
         if player == 'w':
                return False
         elif player =='g':
                return True
    elif computer == 'w':
         if player == 'g':
              return False
         elif player == 's':
              return True  
    elif computer == 'g':
         if player == 's':
             return False
         elif player == 'w':
                return True
print("Computer Turn")                       
rand = random.randint(1, 3)
#print(rand)
if rand==1:
    computer="s"
elif rand==2:
    computer="w" 
if rand==3:
    computer="g"       
player=input("Player Turn \n")
game=snakewatergun(computer,player)    
print(f"Computer {computer}")
print(f"Player {player}")

if game==None:
    print("Game Draw")
elif game:
    print("Player Win")
else:
    print("Player Loose Game")        