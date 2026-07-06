# ==========================================
# Employee Management System (EMS)
# ==========================================

# Dictionary to store employee data
employees = {
    101: {
        "name": "Satya",
        "age": 27,
        "department": "HR",
        "salary": 50000
    },
    102: {
        "name": "Rahul",
        "age": 30,
        "department": "Finance",
        "salary": 60000
    }
}


# ==========================================
# Function to Add Employee
# ==========================================
def add_employee():
    print("\n========== Add Employee ==========")

    while True:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("❌ Employee ID already exists! Please enter another ID.")
        else:
            break

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("\n✅ Employee added successfully!")


# ==========================================
# Function to View Employees
# ==========================================
def view_employees():

    print("\n========== Employee List ==========")

    if len(employees) == 0:
        print("No employees available.")
        return

    print("-" * 70)
    print("{:<10} {:<20} {:<8} {:<15} {:<10}".format(
        "ID", "Name", "Age", "Department", "Salary"))
    print("-" * 70)

    for emp_id, details in employees.items():

        print("{:<10} {:<20} {:<8} {:<15} {:<10}".format(
            emp_id,
            details["name"],
            details["age"],
            details["department"],
            details["salary"]
        ))

    print("-" * 70)


# ==========================================
# Function to Search Employee
# ==========================================
def search_employee():

    print("\n========== Search Employee ==========")

    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:

        emp = employees[emp_id]

        print("\nEmployee Found")
        print("--------------------------")
        print("Employee ID :", emp_id)
        print("Name        :", emp["name"])
        print("Age         :", emp["age"])
        print("Department  :", emp["department"])
        print("Salary      :", emp["salary"])

    else:
        print("\n❌ Employee not found.")


# ==========================================
# Main Menu
# ==========================================
def main_menu():

    while True:

        print("\n===================================")
        print("  EMPLOYEE MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            print("\nThank you for using Employee Management System.")
            print("Program Closed Successfully!")
            break

        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 4.")


# ==========================================
# Program Starts Here
# ==========================================
main_menu()