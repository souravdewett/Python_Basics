"""
Print the following pattern :
        1
       12
      123
     1234
    12345
"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()