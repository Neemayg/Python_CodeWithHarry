import random
'''
-1 for Snake
1 for Water 
0 for Gun

'''
print("Hey Lets Play a fun game which is snake water gun remember we used to play it in our childhood.............")
computer=random.choice([-1,1,0])
youstr=(input("Enter your choice 's' for Snake 'w' for Water 'g' for Gun: "))
youdict={'s':-1 , 'w':1 , 'g':0}
reversedict={-1:'Snake' , 1:'Water' , 0:'Gun'}
if youstr not in youdict:
    print(f"Invalid input! You must enter one of 's', 'w', or 'g'")
else:
    you = youdict[youstr]
print(f"You have chosen {reversedict[you]} and computer have chosen {reversedict[computer]} now lets see who wins!! ")
if computer==you:
  print("You and computer both selected same weapon play again")
else:
  if (computer==-1 and you==1):
    print("Snake drinks the water YOU LOOSE")
  elif (computer==-1 and you==0):
    print("Gun kills the snake YOU WIN!")
  elif (computer==1 and you==-1):
    print("Snake drinks the water YOU WIN!")
  elif (computer==1 and you==0):
    print("Gun is drowned in the water YOU LOOSE")
  elif (computer==0 and you==1):
    print("Gun is drowned in the water YOU WIN!")
  elif (computer==0 and you==-1):
    print("Gun kills the snake YOU LOOSE!")
  else:
    print("uh-oh something went wrong try again!!")