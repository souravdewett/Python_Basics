"""Write a program to calculate bill. Ask the final amount from the user.
    You have to give discount based on the following criteria:
    1. If the bill is greater than 50000, give a discount of 30%
    2. If the bill is between 40000 - 49999, give a discount of 25%
    3. If the bill is between 30000 - 39999, give a discount of 20%
    4. If the bill is between 10000 - 29999, give a discount of 10%
    5. If the bill is less than 10000, No discount
    
    print the discount and final amount to be paid by the user.
"""

num1 = float(input("Enter the final amount of bill = "));
if num1 >= 50000 :
    discount = 30;
elif num1 >= 40000 and num1<= 49999 :
    discount = 25;
elif num1 >= 30000 and num1<= 39999 :
    discount = 20;
elif num1 >= 10000 and num1<= 29999 :
    discount = 10;
else :
    discount = 0;
    
print(f"You got {discount}% discount");
finalamount = num1 - (discount * num1 / 100);
print(f"The final amount to be paid is {finalamount}");