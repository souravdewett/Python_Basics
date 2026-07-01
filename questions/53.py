"""
Ask two numbers from user, if x<y print all the numbers from x to y.
if y<x then print all the numbers from y to x
"""

x = int(input("Enter x"));
y = int(input("Enter y"));
i = 1;
if(x < y) :
    while (x <= y) :
        print(x);
        x = x + 1;
elif(y < x) :
    while(y <= x) :
        print(y);
        y = y + 1;
else :
    print(x);