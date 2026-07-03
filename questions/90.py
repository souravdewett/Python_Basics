"""
Print the following pattern :
        * * * * * * * * *
          * * * * * * *
            * * * * *
              * * *
                * 
                
"""

rows = 10

for i in range(rows):
  # leading spaces increase each row
  for j in range(i):
    print(" ", end=" ")
  # number of stars decreases: 2*(rows-i)-1
  for k in range(2 * (rows - i) - 1):
    print("*", end=" ")
  print()
