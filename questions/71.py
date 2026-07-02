"""
Ask user for n number of lines then print the following pattern :
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
"""

n = int(input("Enter number of lines to print "));

for i in range(1, n) :
    for j in range(1, 6) :
        print(i, end= " ");
    print();