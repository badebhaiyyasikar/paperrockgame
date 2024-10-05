"""
WORKFLOW OF PROJECT:
1-INPUT FORM USER (USER, PAPER, SCISSOR )
2-COMPUTER CHOICE (COMPUTER WILL CHOOSE RANDOMLY NOT CONDITIONALLY)
3- RESULT PRINT

Case :
A- Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock win 

B - Paper
Paper - Paper = tie
Paper - Rock  = Paper win
Paper - Scissor = Scissor Win

C - Scissor 
scissor - Scissor = tie 
Scissor - Rock = Rock win 
Scissor - Paper = Scissorwin



"""
import random
item_list =["Rock", "Paper", "Scissor" ]
user_choice = input("Enter your move = Rock, Ppaer, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Compuetr choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("papers covers Rock, = Computer")
    else:
        print("Rock samshes Scissor, = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, = Computer win")
    else:
        print("Paper cover  Rock, = You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper, = You win")
    else:
        print("Rock samshes  scissor, = computer win")




print("game made for sandeep kumawat")