"""
Ask two numbers x and y from the user . if x<y then print all the numbers from x to y 
if y<x then print all the numbers from y to x
"""

x = int(input("Enter x "));
y = int(input("Enter y"));

if(x < y ) :
    for i in range (x,y) :
        print(i);
elif (y<x) :
    for i in range (y, x) :
        print(i);
