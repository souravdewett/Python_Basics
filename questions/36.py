"""
Take three numbers as input from user and print which one is greater or are they equal.
"""
num1 = int(input("Enter first number"));
num2 = int(input("Enter second number"));
num3 = int(input("Enter third number"));
num4 = int(input("Enter fourth number"));

if(num1 > num2 and num1 > num3 and num1 > num4) :
    print(f"Number {num1} is the greater");
elif(num2 > num1 and num2 > num3 and num2 > num4) :
    print(f"Number {num2} is the greater")
elif(num3 > num1 and num3 > num2 and num3 > num4) :
    print(f"Number {num3} is the greater")
elif(num4 > num1 and num4 > num2 and num4 > num3):
    print(f"Number {num4} is the greater")
else :
    print("Numbers are equal");