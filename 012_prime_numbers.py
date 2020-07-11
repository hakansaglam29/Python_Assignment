number = input("Please enter a number: ")
sum = 0
while not number.isdecimal():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a number: ")