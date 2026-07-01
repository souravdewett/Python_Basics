"""
Write a program that prints "fizz" if number is divisible by 3.
that prints "buzz" if number is divisible by 5.
that prints "fizzbuzz" if number is divisible by both.
print the number itself if none of the conditions are true.
"""

num = int(input("Enter a number"));

if(num % 3 == 0 and num % 5 == 0) :
    print("fizzbuzz");
elif(num % 3 == 0) :
    print("fizz");
elif(num % 5 == 0) :
    print("buzz");
else :
    print(num);
