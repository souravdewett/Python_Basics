"""
Ask 4 numbers from user. Make sure all the numbers are different. Print the smallest number.
"""

num1 = int(input("Enter first number"));
num2 = int(input("Enter second number"));
num3 = int(input("Enter third number"));
num4 = int(input("Enter fourth number"));

if(num1 < num2 and num1 < num3 and num1 < num4) :
    print(f"Number {num1} is the smallest");
elif(num2 < num1 and num2 < num3 and num2 < num4) :
    print(f"Number {num2} is the smallest")
elif(num3 < num1 and num3 < num2 and num3 < num4) :
    print(f"Number {num3} is the smallest")
else :
    print(f"Number {num4} is the smallest")