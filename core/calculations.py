# ----------------------------------------
# Core Logic for Grade & GPA Calculations
# ----------------------------------------

def calculate_percentage(marks_obtained, total_marks):
    if marks_obtained > total_marks or marks_obtained < 0 or total_marks <= 0:
        return None, "Invalid"

    percentage = (marks_obtained / total_marks) * 100

    # Determine grade
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    return percentage, grade


# ------------------------
# GPA Calculation (New)
# ------------------------
def calculate_gpa(subject_grades):
    """
    subject_grades = list of grades A, B, C, D
    GPA Mapping:
        A = 4.0
        B = 3.0
        C = 2.0
        D = 1.0
    """
    grade_map = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0
    }

    total_points = 0
    for grade in subject_grades:
        if grade not in grade_map:
            return None  # invalid grade
        total_points += grade_map[grade]

    gpa = total_points / len(subject_grades)
    return round(gpa, 2)
