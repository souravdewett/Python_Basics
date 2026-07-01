num1 = int(input("Enter a Number = "));

if (num1 % 2 == 0 and num1 % 3 == 0 and num1 % 8 != 0) :
    print("Number is divisible by 2 3 and not 8");
elif (num1 % 2 == 0 and num1 % 3 == 0 and num1 % 8 == 0) : 
    print("Number is divisible by 2 3 and 8");
else :
    print("INVALID ENTRY");

