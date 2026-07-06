"""
Employee Management System (EMS)
---------------------------------
A simple console-based application to manage employee data using
dictionaries, functions, and basic control structures.
"""

# ---------------------------------------------------------
# Step 1: Data Storage
# ---------------------------------------------------------
# Dictionary to store employee data.
# Key   -> emp_id (int)
# Value -> dict with keys: name, age, department, salary

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ravi', 'age': 32, 'department': 'IT', 'salary': 65000},
    103: {'name': 'Anjali', 'age': 29, 'department': 'Finance', 'salary': 58000},
}


# ---------------------------------------------------------
# Step 3: Add Employee Functionality
# ---------------------------------------------------------
def add_employee():
    """Prompt the user for employee details and add them to the dictionary."""
    print("\n--- Add New Employee ---")

    # Validate Employee ID (must be a unique integer)
    while True:
        emp_id_input = input("Enter Employee ID: ").strip()
        if not emp_id_input.isdigit():
            print("Invalid input. Employee ID must be a number.")
            continue

        emp_id = int(emp_id_input)
        if emp_id in employees:
            print(f"Employee ID {emp_id} already exists. Please enter a different ID.")
        else:
            break

    # Validate Name
    while True:
        name = input("Enter Employee Name: ").strip()
        if name == "":
            print("Name cannot be empty.")
        else:
            break

    # Validate Age
    while True:
        age_input = input("Enter Employee Age: ").strip()
        if not age_input.isdigit() or int(age_input) <= 0:
            print("Invalid input. Please enter a valid positive number for age.")
        else:
            age = int(age_input)
            break

    # Validate Department
    while True:
        department = input("Enter Employee Department: ").strip()
        if department == "":
            print("Department cannot be empty.")
        else:
            break

    # Validate Salary
    while True:
        salary_input = input("Enter Employee Salary: ").strip()
        try:
            salary = float(salary_input)
            if salary < 0:
                print("Salary cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for salary.")

    # Store the employee record
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"\nEmployee '{name}' (ID: {emp_id}) added successfully!")


# ---------------------------------------------------------
# Step 4: View All Employees
# ---------------------------------------------------------
def view_employees():
    """Display all employees in a table-like format."""
    print("\n--- Employee List ---")

    if not employees:
        print("No employees available.")
        return

    # Table header
    print(f"{'ID':<10}{'Name':<20}{'Age':<6}{'Department':<15}{'Salary':<10}")
    print("-" * 61)

    # Table rows
    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<6}"
              f"{details['department']:<15}{details['salary']:<10}")


# ---------------------------------------------------------
# Step 5: Search for an Employee by ID
# ---------------------------------------------------------
def search_employee():
    """Search for an employee by their ID and display their details."""
    print("\n--- Search Employee ---")

    emp_id_input = input("Enter Employee ID to search: ").strip()
    if not emp_id_input.isdigit():
        print("Invalid input. Employee ID must be a number.")
        return

    emp_id = int(emp_id_input)

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"ID:         {emp_id}")
        print(f"Name:       {details['name']}")
        print(f"Age:        {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary:     {details['salary']}")
    else:
        print("Employee not found.")


# ---------------------------------------------------------
# Step 2 & 6: Main Menu System
# ---------------------------------------------------------
def main_menu():
    """Display the main menu and route to the appropriate function."""
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main_menu()