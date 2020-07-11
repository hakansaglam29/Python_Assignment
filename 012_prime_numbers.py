number = input("Please enter a number: ")
while not number.isdecimal():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a number: ")
if int(number)==2:
    print("{} is a prime number".format(number))
elif int(number)==1 or int(number)>2 and int(number)%2==0:
     print("{} is not a prime number".format(number))  
elif int(number)>2:
    for i in range(3,(int(number)+1),2):
        if int(number)%i==0:
            if int(number)==i:
                print("{} is a prime number".format(number))
            else:
                print("{} is not a prime number".format(number))
                break          