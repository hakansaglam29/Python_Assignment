number = input("Please enter a number: ")
sum = 0
while not number.isdecimal():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a number: ")
if number.isnumeric():
    for i in range(len(number)):
         sum += int(number[i])**len(number)  
    if  sum == int(number):
         print("{} is an Armstrong number".format(int(number)))
    else:
        print("{} is not an Armstrong number".format(int(number)))

# Find out if a given number is an "Armstrong Number".

# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
# 371 = 33 + 73 + 13;
# 9474 = 94 + 44 + 74 + 44;
# 93084 = 95 + 35 + 05 + 85 + 45.

# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.  