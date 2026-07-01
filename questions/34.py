number_of_classes_held = int(input("Enter Number of Classes Held"));
number_of_classes_attended = int(input("Enter Number of Classes Attended"));

classes_attended_percentage = number_of_classes_attended / number_of_classes_held * 100;

print(int(classes_attended_percentage));

if classes_attended_percentage >= 75 :
    print("Student is eligible to sit in exam.");
else :
    print("Student is not eligible to sit in exam");