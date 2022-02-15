#Hand cricket
import random
print("_________Cricket Match____________")
print("*******************  RULES  ***************")
print("1) Choose any number(score) between 1 to 6 while batting or bowling")
print("2) If Batsman and Bolwer have same score then the batsman is declared Out")
print("Enter the name of player")
name=input()
player_score=0
computer_score=0
flag=0
print(f"{name} vs Computer cricket match")
print("_________This is Toss Time___________")
print("Choose 1 for Odd")
print("Choose 2 for Even")
x=int(input())
if(x<1 or x>2):
    print("Select valid option")    
    x=int(input())    
print("Enter a number")    
y=int(input())    
z=random.randrange(1,7)
if((y+z)%2==0 and x==2):
    print("You won the toss")
    flag=1
elif ((y+z)!=0 and x==1):
    print("You won the toss")   
    flag=1 
else:
    print("Computer won the Toss")    
    lst=["Batting","Bowling"]
    z=random.choice(lst)    
    print("Computer has decided for",z," first")
    if(z=="Batting"):
        print("You have to Bowl first")
        print("**********  FIRST INNING STARTS  **********")
        print("Enter score")
        num=int(input())
        if(num>6):
            print("Enter Score between 1 and 6")
            num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps Computer is Duck")
        while(z!=num):
            computer_score=computer_score+z
            print("Computer Scores:",z)
            print("Total runs:",computer_score)
            if(z==6):
                print("Wow it is six")     
            num=int(input())
            if(num>6):
                print("Enter Score between 1 and 6")
                num=int(input())
            z=random.randrange(1,7)
        print("Computer is out after scoring",computer_score,"runs")
        if(computer_score>=50 and computer_score<100):
                print("Congratulations for fifty\nComputer score:",computer_score)  
        if(computer_score>=100):
                print("Congratulations for Hundred\nComputer score:",computer_score)  
        print("Target for you is",computer_score+1,"runs")
        print("\n*********  SECOND INNING STARTS  *********** ")    
        print("Your batting Starts\ncomputer is bolwing\nEnter score")
        num=int(input())
        if(num>6):
            print("Enter Score between 1 and 6")
            num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps you are Duck")
        while(z!=num):
            player_score=player_score+num
            print("You Scores:",num)
            print("Total runs:",player_score)
            if(num==6):
                print("Wow it is six")
            if(player_score>=computer_score):
                break    
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7)
        if(player_score>=50 and player_score<100):
                print("Congratulations for fifty\nYour score:",player_score)  
        if(player_score>=100):
                print("Congratulations for Hundred\nYour score:",player_score)     
        if(computer_score<player_score):
            print("You successfully chase the target of",computer_score+1,"runs")      
        if(computer_score>player_score):
            print("You loss the match by",computer_score-player_score,"runs")    
        elif(computer_score==player_score):
            print("Match Drawn")
        else:
            print("Congratulations you won")    
    elif(z=="Bowling"):
        print("You are going to Bat first")
        print("********  FIRST INNING STARTS  **********")
        print("Enter Score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps your are Duck ")
        while(z!=num):
            player_score=player_score+num
            print("You Scores:",num)
            print("Total runs:",player_score)
            if(num==6):
                print("Wow it is six")
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7)
        print("Your are out after scoring",player_score, "runs")
        if(player_score>=50 and player_score<100):
                print("Congratulations for fifty\nYour score:",player_score)  
        if(player_score>=100):
                print("Congratulations for Hundred\nYour score:",player_score) 
        print("Target for computer is",player_score+1,"runs")
        print("\n*********  SECOND INNING STARTS  *********** ")  
        print("Computer batting Starts\nyou are bowling now\nEnter score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Wooo Computer is Duck Out")
        while(z!=num):
            computer_score=computer_score+z
            print("Computer Scores:",z)
            print("Total runs:",computer_score)
            if(z==6):
                print("Wow it is six")
            if(computer_score>=player_score):
                break
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7)    
        if(computer_score>=50 and computer_score<100):
                print("Congratulations for fifty\nComputer score:",computer_score)  
        if(computer_score>=100):
                print("Congratulations for Hundred\nComputer score:",computer_score)       
        if(player_score>computer_score):
            print("Computer is out after Scoring",computer_score,"runs")
            print("Congratulations you won the match by",player_score-computer_score, "runs")    
        elif(computer_score==player_score):
            print("Match Drawn")
        else:
            print("Computer successfully chase the target of",player_score+1, "runs")
            print("Computer won") 

if(flag==1):
    print("Choose 1 for Batting and 2 for Bowling")
    x=int(input())
    if(x==1):
        print("You are going to Bat first")
        print("Computer is bowling")
        print("\n********  FIRST INNING STARTS **********")
        print("Enter score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps your are Duck ")
        while(z!=num):
            player_score=player_score+num
            print("You Scores:",num)
            print("Total runs:",player_score)
            if(num==6):
                print("Wow it is six")
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7)
        print("Your are out after scoring",player_score,"runs")
        if(player_score>=50 and player_score<100):
                print("Congratulations for fifty\nYour score:",player_score)  
        if(player_score>=100):
                print("Congratulations for Hundred\nYour score:",player_score) 
        print("Target for computer is",player_score+1)  
        print("\n*********  SECOND INNING STARTS  *********** ")  
        print("Computer batting Starts\n You are bowling now\nEnter score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Wooo Computer is Duck Out")
        while(z!=num):
            computer_score=computer_score+z
            print("Computer Scores:",z)
            print("Total runs:",computer_score)
            if(z==6):
                print("Wow it is six")
            if(computer_score>=player_score):
                break
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7) 
        if(computer_score>=50 and computer_score<100):
                print("Congratulations for fifty\nComputer score:",computer_score)  
        if(computer_score>=100):
                print("Congratulations for Hundred\nComputer score:",computer_score)       
        if(player_score>computer_score):
            print("Computer is out after scoring",computer_score,"runs")
            print("Congratulations you won the match by",player_score-computer_score,"runs")    
        elif(computer_score==player_score):
            print("Match Drawn")
        else:
            print("Computer successfully chase the target of",player_score+1,"runs")
            print("Computer won") 
    elif(x==2):
        print("You are going to bowl first")
        print("Computer is batting ")
        print("\n********  FIRST INNING STARTS  **********")
        print("Enter score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps Computer is Duck")
        while(z!=num):
            computer_score=computer_score+z
            print("Computer Scores:",z)
            print("Total runs:",computer_score)
            if(z==6):
                print("Wow it is six")
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7)
        print("Computer is out after scoring",computer_score,"runs")
        if(computer_score>=50 and computer_score<100):
                print("Congratulations for fifty\nComputer score:",computer_score)  
        if(computer_score>=100):
                print("Congratulations for Hundred\nComputer score:",computer_score) 
        print("Target for you is",computer_score+1," runs")
        print("\n*********  SECOND INNING STARTS  *********** ")  
        print("Your batting Starts\nComputer is bowling now\nEnter Score")
        num=int(input())
        if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
        z=random.randrange(1,7)
        if(num==z):
            print("Opps you are Duck")
        while(z!=num):
            player_score=player_score+num
            print("You Scores:",num)
            print("Total runs:",player_score)
            if(num==6):
                print("Wow it is six")
            if(player_score>=computer_score):
                break
            num=int(input())
            if(num>6):
             print("Enter Score between 1 and 6")
             num=int(input())
            z=random.randrange(1,7) 
        if(player_score>=50 and player_score<100):
                print("Congratulations for fifty\nYour score:",player_score)  
        if(player_score>=100):
                print("Congratulations for Hundred\nYour score:",player_score)      
        if(computer_score>player_score):
            print("You are out after scoring",player_score,"runs")
            print("You loss the match by",computer_score-player_score,"runs")    
        elif(computer_score==player_score):
            print("Match Drawn")
        else:
            print("You successfully chase the target of",computer_score+1,"runs")
            print("Congratulations you won")       
print("\n*********MATCH SUMMARY**********")            
print(name," score :",player_score,"runs")
print("Computer score :",computer_score,"runs")
if(player_score>computer_score):
    print(name," defeated computer ")
elif(computer_score>player_score):
    print("Computer defeated",name)
else:
    print("Match Drawn")        