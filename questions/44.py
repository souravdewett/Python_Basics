"""
Ask start number and end number from user. print all the numbers in between.
"""

start_number = int(input("Enter start number"));
end_number = int (input("Enter end number"));

while(start_number <= end_number) :
    print(start_number, end = " ");
    start_number = start_number + 1;