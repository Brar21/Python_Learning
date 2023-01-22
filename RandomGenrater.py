import random
randomNumber=random.randint(0,10)
print(randomNumber)
userguess=None  #for define userguess we have to declare
guesses=0
while(userguess!=randomNumber):
    userguess=int(input())
    guesses+=1    
    if(userguess==randomNumber):
        print("Guess Correctly")
    else:
        if(userguess>randomNumber):
            print("Sorry guess smaller number")
        else:            
            print("Sorry guess larger number")


print(f"total guesses {guesses} time")

with open("HighScore.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):        
    with open("HighScore.txt","w") as f:
         f.write(str(guesses))
        