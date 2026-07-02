"""
Ask user for number of lines to print then print the following pattern :
5 5 5 5 5
4 4 4 4 4 
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""

n = int(input("Enter number of lines to print = "));

for i in range(n, 0, -1) :
    for j in range(1, 6) :
        print(i, end= " ");
    print();