import random
range_of_choices = ["Rock", "Paper", "Scissors"]
comp_choise = random.choice(range_of_choices)
tries = 0
while tries <3:
    person_choise = input("Enter your choise: ")
    if person_choise == comp_choise:
        print("Nobody wins, try again!")
    elif person_choise == "Rock" and comp_choise == "Paper":
        print("Congratulations, you won!")
        break
    elif person_choise == "Paper" and comp_choise == "Rock":
        print("Unfortunately, you lost. Try again!")
    elif person_choise == "Rock" and comp_choise == "Scissors":
        print("Congratulations, you won!")
        break
    elif person_choise == "Scissors" and comp_choise == "Rock":
        print("Unfortunately, you lost. Try again!")
    elif person_choise == "Scissors" and comp_choise == "Paper":
        print("Congratulations, you won!")
        break
    elif person_choise == "Paper" and comp_choise == "Scissors":
        print("Unfortunately, you lost. Try again!")
        tries +=1
if tries == 3:
    print("You've reached the maximum number of tries. You lost.")