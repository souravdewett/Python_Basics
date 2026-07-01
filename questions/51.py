"""Ask the user for a number print the multiplication table of that number"""

num = int(input("Enter a number"));

i = 1;
while i <= 10 :
    print(f"{num} * {i} =", num * i);
    i = i + 1;