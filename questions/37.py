"""
Identify if the year is a leap year.
"""

year = int(input("Enter a Year = "));

if (year % 4 == 0 and year % 100 == 0) :
    print("It is not a leap year");
elif (year % 4 == 0 and year % 400 == 0) :
    print("This is a leap year");
elif (year % 4 == 0) :
    print("It is a leap year.");
else :
    print("It is a normal year")
