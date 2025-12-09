import tkinter as tk
from tkinter import messagebox
from core.calculations import calculate_percentage, calculate_gpa


def calculate_percentage_ui():
    try:
        marks = float(entry_marks.get())
        total = float(entry_total.get())

        percentage, grade = calculate_percentage(marks, total)

        if percentage is None:
            messagebox.showerror("Error", "Invalid input values")
            return

        label_result.config(text=f"Percentage: {percentage:.2f}%\nGrade: {grade}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


def open_gpa_window():
    gpa_window = tk.Toplevel(root)
    gpa_window.title("GPA Calculator")
    gpa_window.geometry("350x300")

    tk.Label(gpa_window, text="Enter Grades (A, B, C, D):").pack()

    entry_grades = tk.Entry(gpa_window)
    entry_grades.pack()

    result_label = tk.Label(gpa_window, text="", font=("Arial", 12))
    result_label.pack()

    def calculate_gpa_ui():
        grades_text = entry_grades.get().upper().replace(" ", "")
        grades_list = list(grades_text)

        gpa = calculate_gpa(grades_list)

        if gpa is None:
            messagebox.showerror("Error", "Invalid grades! Use A, B, C, or D.")
            return

        result_label.config(text=f"GPA: {gpa}")

    tk.Button(gpa_window, text="Compute GPA", command=calculate_gpa_ui).pack(pady=10)


def reset_fields():
    entry_marks.delete(0, tk.END)
    entry_total.delete(0, tk.END)
    label_result.config(text="")


# Main GUI
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("350x400")

tk.Label(root, text="Marks Obtained:").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Label(root, text="Total Marks:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

tk.Button(root, text="Calculate % & Grade", command=calculate_percentage_ui).pack(pady=10)
tk.Button(root, text="GPA Calculator", command=open_gpa_window).pack(pady=5)
tk.Button(root, text="Reset", command=reset_fields).pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack()

root.mainloop()
