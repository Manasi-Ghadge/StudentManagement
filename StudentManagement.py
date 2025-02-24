import tkinter as tk
from tkinter import messagebox

# Function to add student
def add_student():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    student_records.insert(tk.END, f"ID: {id}, Name: {name}, Age: {age}, Grade: {grade}")

# Initialize main window
root = tk.Tk()
root.title("Student Management System")

# Labels and Entry Widgets
tk.Label(root, text="Student ID:").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Grade:").grid(row=3, column=0)
grade_entry = tk.Entry(root)
grade_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, columnspan=2)

# Listbox to display student records
student_records = tk.Listbox(root)
student_records.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
