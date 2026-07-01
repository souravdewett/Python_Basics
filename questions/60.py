"""
Calculate how many numbers are divisible by both 6 and 7 between 1 to 200 using for loop.
"""

total = 0;

for i in range (1, 201) :
    if (i % 6 == 0 and i % 7 == 0) :
        total = total + 1;
print(total);