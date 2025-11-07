# 📅 Digital Calendar (2019–2068)
# --------------------------------------------
# Features:
# - Tkinter GUI interface
# - Year/Month dropdown selection
# - Day lookup for any given date
# - Leap year and range validation
# - Highlights today's date

import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime

# ----------------------------
# Helper Functions
# ----------------------------

def find_day_of_week(year, month, day):
    """Return the day name for a given date."""
    try:
        date_obj = datetime(year, month, day)
        return date_obj.strftime("%A")
    except ValueError:
        return None

def update_calendar():
    """Update the calendar display based on the selected year and month."""
    try:
        # Get selected year and month
        year = int(year_var.get())
        month = month_names.index(month_var.get()) + 1

        # Year range check
        if not (2019 <= year <= 2068):
            messagebox.showerror("Out of Range", "Year must be between 2019 and 2068.")
            return

        # Display month calendar
        cal_text = calendar.TextCalendar(firstweekday=6).formatmonth(year, month)
        calendar_display.config(state='normal')
        calendar_display.delete(1.0, tk.END)
        calendar_display.insert(tk.END, cal_text)
        
        # Highlight today's date if it matches the displayed month/year
        today = datetime.now()
        if year == today.year and month == today.month:
            # The calendar module output has a predictable structure, 
            # so we can find the day number to highlight it.
            day_str = str(today.day)
            start_index = calendar_display.search(day_str, '1.0', tk.END)
            if start_index:
                # Add a tag to highlight today's date
                end_index = f"{start_index}+{len(day_str)}c"
                calendar_display.tag_add("today_highlight", start_index, end_index)
                calendar_display.tag_config("today_highlight", background="#f0e68c", foreground="#2a4d69", font=("Courier", 11, "bold"))

        calendar_display.config(state='disabled')

        # Leap year status
        leap_text = "✅ Leap Year" if calendar.isleap(year) else "❌ Not a Leap Year"
        leap_label.config(text=f"{leap_text} — {year}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_day():
    """Display the day of the week for a specific date."""
    try:
        # Get selected year, month, and day
        year = int(year_var.get())
        month = month_names.index(month_var.get()) + 1
        day = int(day_entry.get())

        if not (2019 <= year <= 2068):
            messagebox.showerror("Out of Range", "Year must be between 2019 and 2068.")
            return

        day_name = find_day_of_week(year, month, day)
        if day_name:
            result_label.config(text=f"📆 {calendar.month_name[month]} {day}, {year} → **{day_name}**")
        else:
            messagebox.showerror("Invalid Date", "The entered date is not valid.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric day.")

# ----------------------------
# GUI Setup
# ----------------------------

root = tk.Tk()
root.title("🕰️ 50-Year Digital Perpetual Calendar")
# Ensure the window is large enough for the content
root.geometry("650x650") 
root.config(bg="#fdf6e3")

# Title
title_label = tk.Label(
    root,
    text="🕰️ 50-Year Digital Calendar (2019–2068)",
    font=("Helvetica", 14, "bold"),
    bg="#fdf6e3",
    fg="#2a4d69"
)
title_label.pack(pady=10)

# Dropdown Frame
frame = tk.Frame(root, bg="#fdf6e3")
frame.pack(pady=10)

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
# Initialize with current date
month_var = tk.StringVar(value=datetime.now().strftime("%B"))
year_var = tk.StringVar(value=str(datetime.now().year))

month_label = tk.Label(frame, text="Month:", font=("Arial", 11), bg="#fdf6e3")
month_label.grid(row=0, column=0, padx=5)
month_menu = ttk.Combobox(frame, textvariable=month_var, values=month_names, width=12, state="readonly")
month_menu.grid(row=0, column=1, padx=5)

year_label = tk.Label(frame, text="Year:", font=("Arial", 11), bg="#fdf6e3")
year_label.grid(row=0, column=2, padx=5)
# Generate years from 2019 to 2068 inclusive
year_menu = ttk.Combobox(frame, textvariable=year_var, values=[str(y) for y in range(2019, 2069)], width=6, state="readonly") 
year_menu.grid(row=0, column=3, padx=5)

update_btn = tk.Button(frame, text="Show Calendar", command=update_calendar, bg="#4CAF50", fg="white", width=15)
update_btn.grid(row=0, column=4, padx=10)

# Calendar Display Box
# Increased height for better display of month calendar
calendar_display = tk.Text(root, height=12, width=60, font=("Courier", 11)) 
calendar_display.pack(pady=10)
calendar_display.config(state='disabled', bg="#fff8e7")

# Leap Year Label
leap_label = tk.Label(root, text="", font=("Arial", 11, "italic"), bg="#fdf6e3", fg="#2a4d69")
leap_label.pack(pady=5)

# Day Lookup Section
lookup_frame = tk.Frame(root, bg="#fdf6e3")
lookup_frame.pack(pady=15)

day_label = tk.Label(lookup_frame, text="Enter Day:", bg="#fdf6e3", font=("Arial", 11))
day_label.grid(row=0, column=0, padx=5)
day_entry = tk.Entry(lookup_frame, width=5)
day_entry.grid(row=0, column=1, padx=5)

day_btn = tk.Button(lookup_frame, text="Find Day of Week", command=get_day, bg="#2a4d69", fg="white", width=18)
day_btn.grid(row=0, column=2, padx=10)

# Result Label - Increased font size for emphasis
result_label = tk.Label(root, text="Select a date to find its day of the week.", font=("Arial", 12, "bold"), bg="#fdf6e3", fg="#444") 
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Designed in Python 🐍 using Tkinter | Accurate 2019–2068",
    font=("Arial", 9, "italic"),
    bg="#fdf6e3",
    fg="#555"
)
footer.pack(side="bottom", pady=10)

# Initial Load - Display the current month/year on startup
update_calendar()

root.mainloop()