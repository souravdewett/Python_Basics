#Question 1
# num1 = int(input("Enter a number"));

# if num1 >= 0 :
#     print("Number is Positive");
# else :
#     print("Number is Negative");

#Question 2
# character = input("Enter a letter");

# if character == "a" or character =="A" or character == "e" or character == "E" or character == "i" or character =="I" or character == "o" or character == "O" or character == "u" or character == "U" :
#     print("Character is Vowel");
# else :
#     print("Character is Consonant");

#Question 3
# num1 = int(input("Enter First Number"));
# num2 = int(input("Enter Second Number"));

# if num1%num2 == 0 :
#     print(num1, "is divisible by", num2);
# else :
#     print("number is not divisible by num2");

#Question 4 
number_of_classes_held = int(input("Enter Number of Classes Held"));
number_of_classes_attended = int(input("Enter Number of Classes Attended"));

classes_attended_percentage = number_of_classes_attended / number_of_classes_held * 100;

print(int(classes_attended_percentage));

if classes_attended_percentage >= 75 :
    print("Student is eligible to sit in exam.");
else :
    print("Student is not eligible to sit in exam");