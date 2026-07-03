"""
Print the following pattern :
              *    
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
"""
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ");
    for k in range((i * 2) - 1):
        print("*", end=" ");
    print();

# rows = 15
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(2 * i - 1):
#         print("*", end=" ")
#     print()