import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        marks = float(entry_marks.get())
        total = float(entry_total.get())

        if marks > total or marks < 0 or total <= 0:
            messagebox.showerror("Error", "Invalid input values")
            return

        percentage = (marks / total) * 100

        # Grade logic
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        label_result.config(text=f"Percentage: {percentage:.2f}%\nGrade: {grade}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# GUI Window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("350x300")

# Labels
tk.Label(root, text="Marks Obtained:").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Label(root, text="Total Marks:").pack()
entry_total = tk.Entry(root)
entry_total.pack()

# Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack()

# Run GUI
root.mainloop()
