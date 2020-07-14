# Create a list consisting of Fibonacci numbers from 1 to 55 \
# using control flow statements.
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fibo = [1,1]
for i in range(0,8):
    fibo.append(fibo[i]+fibo[i+1])
print(fibo)