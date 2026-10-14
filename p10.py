"""
Age Calculator App
Assignment: Tkinter Geometry Managers
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ── AGE CALCULATION FUNCTION ─────────────────────────────────
def calculate_age():
    """Calculates the user's age based on date, month, and year inputs."""
    name = entry_name.get().strip()
    day_str = entry_day.get().strip()
    month_str = entry_month.get().strip()
    year_str = entry_year.get().strip()
    
    # Validate inputs
    if not name or not day_str or not month_str or not year_str:
        messagebox.showerror("Error", "All fields must be filled out!")
        return
        
    try:
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
        
        # Validate date using datetime
        birth_date = datetime(year, month, day)
        today = datetime.now()
        
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
            
        # Calculate exact age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        if age_days < 0:
            age_months -= 1
        if age_months < 0:
            age_years -= 1
            age_months += 12
            
        # Display personalized message
        result_label.config(
            text=f"Hello, {name}!\nYou are {age_years} years, {age_months} months, and {age_days} days old."
        )
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for day, month, and year.")

def clear_fields():
    """Clears all entries and the result label."""
    entry_name.delete(0, tk.END)
    entry_day.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    result_label.config(text="")

# ── MAIN WINDOW SETUP ────────────────────────────────────────
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.config(bg="#f3f4f6")  # Light gray background color
root.resizable(False, False)

# ── WIDGETS LAYOUT ───────────────────────────────────────────

# Title Header
title_label = tk.Label(
    root, 
    text="🎂 Age Calculator", 
    font=("Arial", 16, "bold"), 
    bg="#f3f4f6", 
    fg="#1f2937"
)
title_label.pack(pady=15)

# Frame for form inputs
form_frame = tk.Frame(root, bg="#f3f4f6")
form_frame.pack(pady=5)

# Name Input Row
lbl_name = tk.Label(form_frame, text="Name:", font=("Arial", 11), bg="#f3f4f6", fg="#374151")
lbl_name.grid(row=0, column=0, sticky="w", pady=8, padx=5)
entry_name = tk.Entry(form_frame, font=("Arial", 11), width=18, bd=1, relief="solid")
entry_name.grid(row=0, column=1, pady=8, padx=5)

# Date Input Row (Day)
lbl_day = tk.Label(form_frame, text="Birth Day (DD):", font=("Arial", 11), bg="#f3f4f6", fg="#374151")
lbl_day.grid(row=1, column=0, sticky="w", pady=8, padx=5)
entry_day = tk.Entry(form_frame, font=("Arial", 11), width=18, bd=1, relief="solid")
entry_day.grid(row=1, column=1, pady=8, padx=5)

# Month Input Row
lbl_month = tk.Label(form_frame, text="Birth Month (MM):", font=("Arial", 11), bg="#f3f4f6", fg="#374151")
lbl_month.grid(row=2, column=0, sticky="w", pady=8, padx=5)
entry_month = tk.Entry(form_frame, font=("Arial", 11), width=18, bd=1, relief="solid")
entry_month.grid(row=2, column=1, pady=8, padx=5)

# Year Input Row
lbl_year = tk.Label(form_frame, text="Birth Year (YYYY):", font=("Arial", 11), bg="#f3f4f6", fg="#374151")
lbl_year.grid(row=3, column=0, sticky="w", pady=8, padx=5)
entry_year = tk.Entry(form_frame, font=("Arial", 11), width=18, bd=1, relief="solid")
entry_year.grid(row=3, column=1, pady=8, padx=5)

# Button Frame for Calculate & Clear
button_frame = tk.Frame(root, bg="#f3f4f6")
button_frame.pack(pady=10)

btn_calculate = tk.Button(
    button_frame, 
    text="Calculate Age", 
    font=("Arial", 11, "bold"), 
    bg="#2563eb", 
    fg="white", 
    activebackground="#1d4ed8",
    activeforeground="white",
    padx=10,
    pady=4,
    bd=0,
    command=calculate_age
)
btn_calculate.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(
    button_frame, 
    text="Clear", 
    font=("Arial", 11), 
    bg="#6b7280", 
    fg="white", 
    activebackground="#4b5563",
    activeforeground="white",
    padx=15,
    pady=4,
    bd=0,
    command=clear_fields
)
btn_clear.grid(row=0, column=1, padx=5)

# Result Output Label
result_label = tk.Label()
root, 
text="", 
font=("Arial",)