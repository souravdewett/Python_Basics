"""
Write a program to check if the last digit of a number is divisible by 5
"""

num1 = int(input("Enter a number"));
last_digit = num1 % 10;

if(last_digit % 5 == 0) :
    print("Last digit of the number is divisible by 5");
else :
    print("Last digit of the number is not divisible by 5");

