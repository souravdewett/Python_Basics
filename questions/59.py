"""
Calculate how many numbers are divisible by 7 from 1 to 100 using for loop.
"""

total = 0;

for i in range (1, 100) :
    if(i % 7 == 0) :
        total = total + 1;
print(total);