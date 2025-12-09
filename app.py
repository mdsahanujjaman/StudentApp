def calculate_percentage():
    marks_obtained = float(input("Enter marks obtained: "))
    total_marks = float(input("Enter total marks: "))

    percentage = (marks_obtained / total_marks) * 100
    print("Percentage:", percentage)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)


def calculate_grade_only():
    marks = int(input("Enter marks (0–100): "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Your Grade:", grade)


def main_menu():
    while True:
        print("\n----- STUDENT GRADE CALCULATOR MENU -----")
        print("1. Calculate Percentage & Grade")
        print("2. Grade Only")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate_percentage()
        elif choice == '2':
            calculate_grade_only()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the menu
main_menu()
