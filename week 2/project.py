class StudentDatabase:
    def __init__(self):
        self.students = {}
        
    def add_student(self, name, age, grade):
        self.students[name] = {'Age': age, 'Grade': grade}

    def view_student(self, name):
        if name in self.students:
            print(f"Student: {name}\nAge: {self.students[name]['Age']}\n Grade: {self.students[name]['Grade']}")
        else:
            print(f"Student {name} not found in the database.")

    def list_all_students(self):
        print("List of all students:")
        for name, details in self.students.items():
            print(f"Name: {name}, Age: {details['Age']}, Grade: {details['Grade']}")

    def update_student_info(self, name, age= None, grade=None):
        if name in self.students:
            if age is not None:
                self.students[name]['Age'] = age
            if grade is not None:
                self.students[name]['Grade'] =grade
            print(f"Information for {name} updateed successfully.")
        else:
            print(f"Student {name} not found in the database.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"Student {name} deleted successfully.")
        else:
            print(f"Student {name} not found in the database.")

def main():
    student_db = StudentDatabase()  

    while True:
        print("\nStudent Database Menu:")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Student")
        print("4. Updeate Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ") 

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input ("Enter student grade: ")
            student_db.add_student(name, age, grade)

        elif choice == '2':
            name = input("Enter student name to view: ")
            student_db.view_student(name)

        elif choice == '3':
            student_db.list_all_students()

        elif choice == '4':
            name = input("Enter student name to update: ")
            age = int(input("Enter student age (press Enter to skip): ") or -1)
            grade = input ("Enter student grade (press Enter to skip): ")
            student_db.update_student_info(name, age, grade)

        elif choice == '5':
            name = input("Enter student name to delete: ")
            student_db.delete_student(name)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Error...Invalid choice. please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()   