"""
Calculate factorial of a number using for loop.
"""

num = int(input("Enter a number"));
factorial = 1;

for i in range (1, num) :
    factorial = factorial * i;
    
print(factorial);