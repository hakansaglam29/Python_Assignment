age = bool(input("Are you a cigarette addict older than 75 years old? ")=="Yes")
chronic = bool(input("Do you have a severe chronic disease? ")=="Yes")
immune = bool(input("Is your immune system too weak? ")=="Yes")
if age or chronic or immune == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
# Task : Estimating the risk of death from coronavirus