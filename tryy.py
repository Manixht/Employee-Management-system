employee = {
    101: {
        "name": "Alice Smith",
        "age": 28,
        "position": "Data Analyst",
        "department": "Analytics",
        "salary": 70000,
        "skills": ["Python", "R", "SQL"],
        "address": {
            "street": "456 Elm St",
            "city": "Othertown",
            "state": "NY",
            "zip_code": "67890"
        }
    },
    102: {
        "name": "John Doe",
        "age": 30,
        "position": "Software Engineer",
        "department": "IT",
        "salary": 80000,
        "skills": ["Python", "JavaScript", "SQL"],
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip_code": "12345"
        }
    }
}

print("Employee Data:")
for emp_id, details in employee.items():
    print(f"\nEmployee ID: {emp_id}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Position: {details['position']}")
    print(f"Department: {details['department']}")
    print(f"Salary: ${details['salary']}")
    print("Skills:", ", ".join(details["skills"]))
    address = details["address"]
    print("Address:")
    print(f"  Street: {address['street']}")
    print(f"  City: {address['city']}")
    print(f"  State: {address['state']}")
    print(f"  Zip Code: {address['zip_code']}")