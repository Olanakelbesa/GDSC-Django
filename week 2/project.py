# Student Database Program (Without Functions)

# Initialize an empty dictionary to store student information
students_database = {}

# Main program loop
while True:
    print("\nStudent Database Menu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Add Student
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")

        # Create a dictionary for the student
        student_info = {
            "Name": name,
            "Age": age,
            "Grade": grade
        }

        # Add the student to the database
        students_database[name] = student_info
        print(f"Student {name} added to the database.")

    elif choice == "2":
        # View Student
        name = input("Enter student name to view details: ")
        if name in students_database:
            student_info = students_database[name]
            print(f"\nStudent Details for {name}:\n")
            for key, value in student_info.items():
                print(f"{key}: {value}")
        else:
            print(f"Student {name} not found in the database.")

    elif choice == "3":
        # List All Students
        print("\nList of All Students:\n")
        for name, student_info in students_database.items():
            print(f"Name: {name}, Age: {student_info['Age']}, Grade: {student_info['Grade']}")
        print()

    elif choice == "4":
        # Update Student Information
        name = input("Enter student name to update information: ")
        if name in students_database:
            print(f"\nCurrent Details for {name}:\n")
            for key, value in students_database[name].items():
                print(f"{key}: {value}")

            # Get updated information
            new_age = int(input("\nEnter new age (press Enter to keep current): ") or students_database[name]["Age"])
            new_grade = input("Enter new grade (press Enter to keep current): ") or students_database[name]["Grade"]

            # Update the student information
            students_database[name]["Age"] = new_age
            students_database[name]["Grade"] = new_grade

            print(f"\nInformation for {name} updated.")
        else:
            print(f"Student {name} not found in the database.")

    elif choice == "5":
        # Delete Student
        name = input("Enter student name to delete: ")
        if name in students_database:
            del students_database[name]
            print(f"Student {name} deleted from the database.")
        else:
            print(f"Student {name} not found in the database.")

    elif choice == "6":
        # Exit
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
