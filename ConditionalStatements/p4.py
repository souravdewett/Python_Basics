maths = int(input("Enter Maths Marks"));
science = int(input("Enter Science Marks"));
punjabi = int(input("Enter Punjabi Marks"));
hindi = int(input("Enter Hindi Marks"));
english = int (input("Enter English Marks"));

total_percentage = ((maths + science + punjabi + hindi + english) /500) * 100;
print(total_percentage);

if(total_percentage > 90 and total_percentage <= 100) :
    print("A grade");
elif(total_percentage > 80 and total_percentage <= 90) :
    print("B grade");
elif(total_percentage > 70 and total_percentage <= 80) :
    print("C grade");
elif(total_percentage > 60 and total_percentage <= 70) :
    print("D grade");
elif(total_percentage <=60) : 
    print("Fail");
else :
    print("INVALID");