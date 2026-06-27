# student_management.py

# Dictionary to store all student records
students = {}

def show_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All")
        print("3. Search")
        print("4. Update Marks")
        print("5. Delete")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            roll = input("Enter Roll No: ")
            
            if roll in students:
                print("Error: Student with this Roll No already exists!")
            else:
                name = input("Enter Name: ")
                m1 = float(input("Enter Subject 1 Marks: "))
                m2 = float(input("Enter Subject 2 Marks: "))
                m3 = float(input("Enter Subject 3 Marks: "))
                m4 = float(input("Enter Subject 4 Marks: "))
                m5 = float(input("Enter Subject 5 Marks: "))
                
                # Calculate percentage
                total = m1 + m2 + m3 + m4 + m5
                percentage = total / 5
                
                # Calculate grade
                if percentage >= 90:
                    grade = "O"
                elif percentage >= 80:
                    grade = "A+"
                elif percentage >= 70:
                    grade = "A"
                elif percentage >= 60:
                    grade = "B+"
                elif percentage >= 50:
                    grade = "B"
                else:
                    grade = "F"
                
                # Store in dictionary
                students[roll] = {
                    'name': name,
                    'marks': [m1, m2, m3, m4, m5],
                    'percentage': percentage,
                    'grade': grade
                }
                print("Student added successfully!")

        elif choice == '2':
            print("\n--- All Student Records ---")
            if not students:
                print("No records found.")
            
            for roll, details in students.items():
                print(f"Roll: {roll} | Name: {details['name']} | %: {details['percentage']} | Grade: {details['grade']}")

        elif choice == '3':
            roll = input("Enter Roll No to search: ")
            
            if roll in students:
                d = students[roll]
                print(f"\nStudent Found:")
                print(f"Name: {d['name']}")
                print(f"Marks: {d['marks']}")
                print(f"Percentage: {d['percentage']}%")
                print(f"Grade: {d['grade']}")
            else:
                print("Student not found.")

        elif choice == '4':
            roll = input("Enter Roll No to update marks: ")
            
            if roll in students:
                m1 = float(input("Enter New Subject 1 Marks: "))
                m2 = float(input("Enter New Subject 2 Marks: "))
                m3 = float(input("Enter New Subject 3 Marks: "))
                m4 = float(input("Enter New Subject 4 Marks: "))
                m5 = float(input("Enter New Subject 5 Marks: "))
                
                # Recalculate everything
                total = m1 + m2 + m3 + m4 + m5
                percentage = total / 5
                
                if percentage >= 90:
                    grade = "O"
                elif percentage >= 80:
                    grade = "A+"
                elif percentage >= 70:
                    grade = "A"
                elif percentage >= 60:
                    grade = "B+"
                elif percentage >= 50:
                    grade = "B"
                else:
                    grade = "F"
                
                # Update the dictionary
                students[roll]['marks'] = [m1, m2, m3, m4, m5]
                students[roll]['percentage'] = percentage
                students[roll]['grade'] = grade
                
                print("Marks updated successfully!")
            else:
                print("Student not found.")

        elif choice == '5':
            roll = input("Enter Roll No to delete: ")
            
            if roll in students:
                del students[roll]
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        elif choice == '6':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the program
if __name__ == "__main__":
    show_menu()