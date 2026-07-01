"""
Calculate factorial of a number entered by user
"""

num = int(input("Enter a number"));
i = 1;
factorial = 1;

while(i <= num) :
    factorial = factorial * i;
    i = i + 1;
print(factorial);
