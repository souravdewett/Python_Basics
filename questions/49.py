"""
Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50
"""

i = 20;
divisible_numbers = 0;

while (i <= 50) :
    if(i % 4 == 0) :
        divisible_numbers = divisible_numbers + i;
    i = i + 1;
print(divisible_numbers);
