"""
Calculate how many numbers are divisible by 7 from 1 to 100
"""

i = 1;
divisible_numbers = 0;

while i <= 100 :
    if i % 7 == 0 :
        divisible_numbers = divisible_numbers + 1;
    i = i + 1;
print(divisible_numbers);
