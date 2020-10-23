# A "Perfect Number" is a number in which the sum of its factors (excluding itself) are equal to itself.
# Write a function that can verify if the given integer is a perfect number.
# Example
# 28 has the following factors: 1, 2, 4, 7, 14
# 1 + 2 + 4 + 7 + 14 = 28 therefore 28 is a perfect number!


def perfect_verification(number):
    dividers = [i for i in range(1,number) if number%i==0]
    
    # dividers = []
    # for i in range(1,number):
    #     if number%i == 0:
    #         dividers.append(i)
            
    sum_dividers = 0
    for i in dividers:
        sum_dividers +=i
    if sum_dividers == number: return "It's a perfect number"
    else: return "It's not a perfect number"

print(perfect_verification(28))
