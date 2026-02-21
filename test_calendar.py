import unittest
from unittest.mock import MagicMock, patch
import sys

# Define a mock TclError
class MockTclError(Exception):
    pass

# Mocking tkinter and other dependencies before importing the app
mock_tk = MagicMock()
mock_tk.TclError = MockTclError
sys.modules['tkinter'] = mock_tk

mock_ttk = MagicMock()
sys.modules['tkinter.ttk'] = mock_ttk

mock_messagebox = MagicMock()
sys.modules['tkinter.messagebox'] = mock_messagebox

import my_calendar_app

# Inject mocks into the module
my_calendar_app.tk = mock_tk
my_calendar_app.messagebox = mock_messagebox

class TestCalendarApp(unittest.TestCase):
    def setUp(self):
        # Reset mocks for each test
        my_calendar_app.year_var = MagicMock()
        my_calendar_app.month_var = MagicMock()
        my_calendar_app.calendar_display = MagicMock()
        my_calendar_app.leap_label = MagicMock()
        # Ensure month_names is set (it is defined globally in the module)
        my_calendar_app.month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    def test_update_calendar_valid(self):
        # Set up valid inputs
        my_calendar_app.year_var.get.return_value = "2024"
        my_calendar_app.month_var.get.return_value = "February"

        # Call the function
        my_calendar_app.update_calendar()

        # Verify calendar_display was updated
        my_calendar_app.calendar_display.insert.assert_called()
        # Verify leap year label was updated correctly for 2024
        my_calendar_app.leap_label.config.assert_called_with(text="✅ Leap Year — 2024")

    def test_update_calendar_invalid_year(self):
        # Set up invalid year (out of range)
        my_calendar_app.year_var.get.return_value = "2018"
        my_calendar_app.month_var.get.return_value = "January"

        my_calendar_app.update_calendar()

        # Verify error message was shown
        mock_messagebox.showerror.assert_called_with("Out of Range", "Year must be between 2019 and 2068.")

    def test_update_calendar_value_error(self):
        # Set up something that causes a ValueError, e.g., year is not an int
        my_calendar_app.year_var.get.return_value = "abc"

        my_calendar_app.update_calendar()

        # Verify the new specific exception handling works
        mock_messagebox.showerror.assert_called()
        args, kwargs = mock_messagebox.showerror.call_args
        self.assertEqual(args[0], "Error")
        self.assertIn("invalid literal for int()", args[1])

    def test_update_calendar_tcl_error(self):
        # Set up valid inputs
        my_calendar_app.year_var.get.return_value = "2024"
        my_calendar_app.month_var.get.return_value = "February"

        # Mock a TclError during widget update
        my_calendar_app.calendar_display.config.side_effect = MockTclError("Widget destroyed")

        my_calendar_app.update_calendar()

        # Verify the exception was caught and showed an error message
        mock_messagebox.showerror.assert_called_with("Error", "An error occurred: Widget destroyed")

if __name__ == '__main__':
    unittest.main()
