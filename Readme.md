
🕰️ 50-Year Digital Perpetual Calendar (2019–2068)
This is a standalone desktop application built using Python and the Tkinter library. It provides a perpetual calendar interface allowing users to browse months and years within a 50-year range (2019–2068) and lookup the day of the week for any specific date.

✨ Features
GUI Interface: A clean, themed user interface built with tkinter.

Year/Month Navigation: Use dropdown menus to instantly switch between months and years.

50-Year Range: Accurately displays calendars from 2019 to 2068.

Day Lookup: Input a specific day number to find the corresponding day of the week (e.g., "Monday", "Friday").

Validation: Includes checks for valid dates and ensures the year is within the allowed range.

Leap Year Indicator: Clearly shows whether the selected year is a leap year.

Current Date Highlight: Automatically highlights today's date if the current month and year are selected.

🚀 Getting Started
Prerequisites
You need Python 3.x installed on your system. Tkinter is typically included with standard Python installations on most operating systems.

Installation and Setup
Save the Code: Save the provided Python code into a file named perpetual_calendar.py (or any name except calendar.py to avoid import errors).

Run the Application: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

Bash

python my_calendar_app.py
The calendar application window should open immediately.

⚙️ How to Use
Select a Date: Use the Month and Year dropdown menus at the top of the window to choose the desired time frame.

Show Calendar: Click the Show Calendar button to update the main display with the calendar grid for the selected month.

Find Day of Week:

Ensure the desired year and month are selected in the dropdowns.

Enter a day number (e.g., 15) into the Enter Day field.

Click the Find Day of Week button.

The result will be displayed below, showing the exact day name (e.g., "Monday").

📝 Code Structure
The script is organized into three main sections:

Helper Functions: Contains core logic like find_day_of_week and the main update functions (update_calendar, get_day).

GUI Setup: Initializes the main window (root), creates all the widgets (labels, buttons, dropdowns), and manages the layout using .pack() and .grid().

Initial Load: The script concludes by calling update_calendar() to load the current month/year upon startup and starting the tkinter event loop (root.mainloop()).

Note on Leap Years: The application uses Python's built-in calendar.isleap() function for accurate leap year determination.