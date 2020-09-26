import random
print("*******   Welcome To Snake Water Game   ********")
print("s = Snake\n g = gun\n w = water\n")
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        
    
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
         return True
    elif comp=='g':
        if you=='w':
            return False
        elif you=='s':
            return True
        
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
n = random.randint(1,3)
if n==1:
    comp ='s'
elif n==2:
    comp = 'w'
elif n==3:
    comp ='g'
    
you = input("Your Turn: Snake(s) Water(w) or Gun(g)")
a = gamewin(comp,you)

print(f"Computer choose{comp}")
print(f"you choose{you}")

if a==None:
    print("The Game is tie")
elif a:
    print("you won the game")
else:
    print("You loose")    
    

        
        
        