"""
Ask a user for a number, print the multiplication table of that number using for loop.
"""

num = int(input("Enter a number"));

for i in range (1, 11) :
    print(f"{i} * {num} = ", i * num);
