
Qs=input("Do you want to play Quize game!?\n")

if Qs =="Yes":
    print(" Ok!Lets Play...:)\n")
    print(" Some information :- 1. 1st letter of your answer should be capital letter \n 2.No negative marks \n")

else:
    quit()
    
score=0
score1=0   
#1st round 
#1st qs
ans=input("1. Who discovered Protons?\n")
if ans==("Rutherford"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")

#2nd qs
ans=input("2. What does Big Bang theory explain ?\n")
if ans==("Origin of universe"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")

#3rd qs
ans=input("3. Name the smallest Ocean.\n")
if ans==("Arctic Ocean"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")

#4th qs
ans=input("4. At which temperature does water boil?\n")
if ans==("100◦C"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")
    
#5th qs
ans=input("5. Who is the king of the Jungle?\n")
if ans==("Lion"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")
    
 #6th qs   
ans=input("6. How many players are there in each side of a Hockey team?\n")
if ans==("11"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")
    
#7th qs
ans=input("7. How many states are there in India?\n")
if ans==("29"):
    print('Correct :)')
    score +=1
else:
    print("Incorrect!:(")

p = ((score/7)*100)
print("You got " + str(score) +" questions correct :)")
print("You got " + str(p) +" %.")    



if p >= 10:
    print("Hurrah!!!! You won the 1st round !! so lets play Next Round :)\n")
else:
    print("OOPs sorry :( you can't play next round!!:( \n Try again!\n")
    quit()

#second round  
#1st qs 
 
ans=input("1. How many bones do we have?\n")
if ans==("206"):
    print('Correct :)')
    score1 +=2
else:
    print("Incorrect!:(")
    
    
#2nd 
ans=input("2. Cataract is what type of  disease .\n")
if ans==("Eye"):
    print('Correct :)')
    score1 +=2
else:
    print("Incorrect!:(")
    

#3rd    
ans=input("3. Which is the first Asian country to orbit Mars?\n")
if ans==("India"):
    print('Correct :)')
    score1 +=2
else:
    print("Incorrect!:(")

#4th  
ans=input("4. Where are the HeadQuarters of UNESCO?\n")
if ans==("Paris, France"):
    print('Correct :)')
    score1 +=2
else:
    print("Incorrect!:(")    
    
q = ((score1/4)*100)
print("You got " + str(score1) +" questions correct :)\n")
print("You got " + str(q) +" %.\n")    


print("Thankyou for playing our Quize game!!!! :)")


    