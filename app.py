marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))

percentage = (marks_obtained / total_marks) * 100
print("Percentage:", percentage)

# Grade calculation based on percentage
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
