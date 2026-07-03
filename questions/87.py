"""
Print the following pattern
        1
       22
      333
     4444
    55555
"""

for i in range(1,6) :
    for j in range(i, 6) :
        print(" ", end = " ");
    for k in range(1, i + 1) :
        print(i, end = " ");
    print();