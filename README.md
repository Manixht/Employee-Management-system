This project is actually very simple if we divide it into small steps.

Project Overview

We'll build a program like this:

========== Employee Management System ==========
1. Add Employee
2. View All Employees
3. Search Employee
4. Exit

Enter your choice:

Everything will be stored in a dictionary.

Step 1: Create a Project Folder

Create a folder named:

Employee_Management_System

Inside it create one file:

ems.py

Open it in VS Code.

Step 2: Create Employee Dictionary

The assignment says:

Store employee data in a dictionary.

Write:

employees = {
    101: {
        "name": "Satya",
        "age": 27,
        "department": "HR",
        "salary": 50000
    }
}
What does this mean?
employees
│
├──101
│   ├── name = Satya
│   ├── age = 27
│   ├── department = HR
│   └── salary = 50000

Later you'll add more employees like:

101
102
103
104
Step 3: Print the Menu

Now create a function.

def main_menu():
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

Run it.

Output:

===== Employee Management System =====

1. Add Employee
2. View Employees
3. Search Employee
4. Exit
Step 4: Ask User Choice

Below the menu write:

choice = input("Enter your choice: ")

Now if user types

1

Python stores

choice = "1"
Step 5: Use while Loop

The assignment says:

Keep showing menu until Exit.

So:

while True:

    main_menu()

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you!")
        break

Now program runs forever until user enters

4
Step 6: Add Employee Function

Create a new function.

def add_employee():

Inside it ask user:

emp_id = int(input("Enter Employee ID: "))

Then

name = input("Enter Name: ")

Then

age = int(input("Enter Age: "))

Then

department = input("Enter Department: ")

Then

salary = float(input("Enter Salary: "))
Step 7: Check Duplicate Employee ID

Before adding:

Is Employee ID already present?

Example

101

Already exists.

So

Please enter another Employee ID.

Use:

if emp_id in employees:

Otherwise

Add employee.

Step 8: Store Employee

Save data like this:

employees[emp_id] = {
    ...
}

Now dictionary becomes

101

102

103
Step 9: View Employees Function

Create

def view_employees():

If dictionary empty

Print

No employees available.

Otherwise

Loop through dictionary.

Use

for emp_id, details in employees.items():

Print

101

Satya

27

HR

50000



Then next employee.

Step 10: Search Employee

Create

def search_employee():

Ask

Enter Employee ID

If exists

Show

Name

Age

Department

Salary

Otherwise

Employee not found.
Step 11: Connect Everything

Inside

while True

Write

If choice is 1

↓

Call add_employee()

If choice is 2

↓

Call view_employees()

If choice is 3

↓

Call search_employee()

If choice is 4

↓

Exit
Final Project Flow
Start

↓

Show Menu

↓

User Choice

↓

1

↓

Add Employee

↓

Back to Menu

↓

2

↓

View Employees

↓

Back

↓

3

↓

Search

↓

Back

↓

4

↓

Exit