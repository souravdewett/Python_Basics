"""
Take salary as input from user and update the salary of the employee
"""

salary = float(input("Enter the Salary "));

if salary < 10000 :
    increment = 5;
elif salary > 10000 and salary < 20000 :
    increment = 10;
elif salary > 20000 and salary < 50000 :
    increment = 15
else:
    increment = 20
    
final_salary = salary + (increment * salary / 100);
print(f"Final Salary is {final_salary}");
