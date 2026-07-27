print("Welcome to the student data organizer!")



students = {}

while True:
    print("\n===== Student Data Organizer =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Student ID: ")

        if sid in students:
            print("Student ID already exists!")
            continue

        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        subjects = [subject.strip() for subject in subjects]

        students[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- Display All Students ---")
            for sid, info in students.items():
                print(f"Student ID: {sid}")
                print(f"Name: {info['name']}")
                print(f"Age: {info['age']}")
                print(f"Grade: {info['grade']}")
                print(f"DOB: {info['dob']}")
                print("Subjects:", ", ".join(info['subjects']))
                print("-" * 30)

    elif choice == "3":
        sid = input("Enter Student ID to update: ")

        if sid in students:
            print("Leave blank if no change.")

            name = input("New Name: ")
            age = input("New Age: ")
            grade = input("New Grade: ")
            dob = input("New DOB: ")
            subjects = input("New Subjects (comma-separated): ")

            if name:
                students[sid]["name"] = name
            if age:
                students[sid]["age"] = int(age)
            if grade:
                students[sid]["grade"] = grade
            if dob:
                students[sid]["dob"] = dob
            if subjects:
                students[sid]["subjects"] = [s.strip() for s in subjects.split(",")]

            print("Student information updated successfully!")
        else:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")

        if sid in students:
            del students[sid]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        all_subjects = set()

        for info in students.values():
            all_subjects.update(info["subjects"])

        if all_subjects:
            print("\nSubjects Offered:")
            for subject in sorted(all_subjects):
                print(subject)
        else:
            print("No subjects available.")

    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")

