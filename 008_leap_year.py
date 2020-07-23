number = int(input("Please enter a year: "))
if number % 400 == 0 or number % 100 != 0 and number % 4 == 0:
    print(f"{number} is a leap year")
else:
    print(f"{number} is not a leap year")
    