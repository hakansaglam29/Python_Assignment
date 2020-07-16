# Task : Print the FizzBuzz numbers.

# FizzBuzz is a famous code challenge used in interviews to test basic 
# programming skills. It's time to write your own implementation.
# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.
# Output each value on a separate line.
# Note that : This question is famous on the web, so to get
#  more benefit from this assignment, try to complete this task on your own.

for i in range(1,101):
    if i%15==0: print("FizzBuzz")
    elif i%3==0: print("Fizz")
    elif i%5==0: print("Buzz")
    else: print(i)

# s= ["FizzBuzz" if i%15==0  else "Fizz" if i%3==0 else "Buzz"\
#      if i%5==0 else i for i in range(1,101)]
# for i in s: print(i)