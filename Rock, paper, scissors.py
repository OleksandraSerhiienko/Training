import random
range_of_choices = ["Rock", "Paper", "Scissors"]
comp_choise = random.choice(range_of_choices)
tries = 0
while tries < 3:
    person_choise = input("Enter your choise: ")
    if person_choise == comp_choise:
        print("Nobody wins, try again!")
    elif (person_choise == "Rock" and comp_choise == "Paper") or \
        (person_choise == "Paper" and comp_choise == "Scissors") or \
        (person_choise == "Scissors" and comp_choise == "Paper"):
        print("Congratulations, you won!")
        break
    elif person_choise == "Stop":
        break
    else:
        print("Unfortunately, you lost")
        tries += 1 
if tries == 3:
    print("You've reached the maximum number of tries. You lost.")