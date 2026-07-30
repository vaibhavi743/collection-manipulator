print("=" * 50)
print("      Welcome to Student Data Organizer")
print("=" * 50)

students = []

while True:
    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        subject_input = input("Enter Subjects (comma separated): ")

        subjects = set()

        for subject in subject_input.split(","):
            subjects.add(subject.strip())

        student_info = (student_id, dob)

        student = {
            "info": student_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo student records found.")

        else:
            print("\n========== STUDENT RECORDS ==========")

            for student in students:

                print(f"Student ID : {student['info'][0]}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Grade      : {student['grade']}")
                print(f"DOB        : {student['info'][1]}")
                print(f"Subjects   : {', '.join(student['subjects'])}")
                print("-" * 40)

    elif choice == "3":

        sid = input("Enter Student ID to Update: ")

        found = False

        for student in students:

            if student["info"][0] == sid:

                found = True

                print("Leave blank if no change.")

                name = input("New Name: ")
                age = input("New Age: ")
                grade = input("New Grade: ")
                subjects = input("New Subjects (comma separated): ")

                if name != "":
                    student["name"] = name

                if age != "":
                    student["age"] = int(age)

                if grade != "":
                    student["grade"] = grade

                if subjects != "":
                    student["subjects"] = set()

                    for sub in subjects.split(","):
                        student["subjects"].add(sub.strip())

                print("Student information updated successfully!")
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":

        sid = input("Enter Student ID to Delete: ")

        found = False

        for i in range(len(students)):

            if students[i]["info"][0] == sid:

                del students[i]

                print("Student deleted successfully!")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":

        all_subjects = set()

        for student in students:

            all_subjects.update(student["subjects"])

        if len(all_subjects) == 0:
            print("No subjects available.")

        else:

            print("\nSubjects Offered:")

            for subject in sorted(all_subjects):
                print(subject)

    elif choice == "6":

        print("\nThank you for using Student Data Organizer!")
        print("Good Bye!")
        break

    else:
        print("Invalid Choice! Please try again.")
        
