all_students = []

while True:
    print("\nEnter the following details for a student:")
    
    student_data = {
        "Student_Name": input("Enter your Name: "),
        "Roll_Number": int(input("Enter your Roll no: ")),
        "Maths_marks": int(input("Enter your Maths marks: ")),
        "Physics_marks": int(input("Enter your Physics marks: ")),
        "Urdu_marks": int(input("Enter your Urdu marks: ")),
        "English_marks": int(input("Enter your English marks: ")),
        "Computer_marks": int(input("Enter your Computer marks: "))
    }
    

    obtain_marks = (
        student_data["Maths_marks"] +
        student_data["Physics_marks"] +
        student_data["Urdu_marks"] +
        student_data["English_marks"] +
        student_data["Computer_marks"]
    )
    
    total_marks = 500
    percentage = (obtain_marks / total_marks) * 100
    student_data["Percentage"] = percentage
    
    # Add student to list
    all_students.append(student_data)
    
    # Ask if user wants to continue
    print("\n=== Student Entry Complete ===")
    print(f"Total students entered: {len(all_students)}")
    userInput = input("\nDo you want to enter more student data? (Y to proceed / N to see all results): ").upper()
    
    if userInput == 'N':

        print("\n====== RESULTS OF ALL STUDENTS ======")
        
        # Loop through each student in the list, starting index at 1 for better readability
        for index, student in enumerate(all_students, start=1):
            print(f"\nStudent #{index}:")
            print(f"Student Name: {student['Student_Name']}")
            print(f"Roll Number: {student['Roll_Number']}")
            print(f"Marks:")
            print(f"  Maths: {student['Maths_marks']}")
            print(f"  Physics: {student['Physics_marks']}")
            print(f"  Urdu: {student['Urdu_marks']}")
            print(f"  English: {student['English_marks']}")
            print(f"  Computer: {student['Computer_marks']}")
            print(f"Percentage: {student['Percentage']:.2f}%")
            
           
            if student['Percentage'] >= 80:
                grade = "A+"
            elif student['Percentage'] >= 70:
                grade = "A"
            elif student['Percentage'] >= 60:
                grade = "B"
            elif student['Percentage'] >= 50:
                grade = "C"
            else:
                grade = "Failed"
                
            print(f"Grade: {grade}")
            print("=" * 40)
        break
    elif userInput == 'Y':
        print("\nProceeding to next student entry...")
        continue
    else:
        print("Invalid input! Please enter Y or N")
        continue
