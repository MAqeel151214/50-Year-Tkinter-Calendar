import unittest
from unittest.mock import MagicMock, patch
import sys

# Mock tkinter and its components before importing the app
sys.modules['tkinter'] = MagicMock()
sys.modules['tkinter.ttk'] = MagicMock()
sys.modules['tkinter.messagebox'] = MagicMock()
sys.modules['tkinter'].messagebox = sys.modules['tkinter.messagebox']

import my_calendar_app

# Ensure we're testing with the mock
my_calendar_app.messagebox.showerror = MagicMock()

class TestSecurityFix(unittest.TestCase):
    def setUp(self):
        # Reset mocks
        my_calendar_app.messagebox.showerror.reset_mock()

        # Manually assign mocked variables that are usually created in if __name__ == "__main__":
        my_calendar_app.year_var = MagicMock()
        my_calendar_app.month_var = MagicMock()
        my_calendar_app.day_entry = MagicMock()
        my_calendar_app.calendar_display = MagicMock()
        my_calendar_app.leap_label = MagicMock()
        my_calendar_app.result_label = MagicMock()

    def test_update_calendar_generic_error(self):
        # Force an unexpected exception
        my_calendar_app.year_var.get.side_effect = RuntimeError("Sensitive internal detail")

        my_calendar_app.update_calendar()

        # Verify that showerror was called with a generic message, NOT the sensitive detail
        my_calendar_app.messagebox.showerror.assert_called_once()
        args, _ = my_calendar_app.messagebox.showerror.call_args
        self.assertEqual(args[0], "Error")
        self.assertEqual(args[1], "An unexpected error occurred. Please try again.")
        self.assertNotIn("Sensitive internal detail", args[1])

    def test_get_day_generic_error(self):
        # Force an unexpected exception
        my_calendar_app.year_var.get.side_effect = RuntimeError("Another sensitive detail")

        my_calendar_app.get_day()

        # Verify that showerror was called with a generic message
        my_calendar_app.messagebox.showerror.assert_called_once()
        args, _ = my_calendar_app.messagebox.showerror.call_args
        self.assertEqual(args[0], "Error")
        self.assertEqual(args[1], "An unexpected error occurred. Please try again.")
        self.assertNotIn("Another sensitive detail", args[1])

if __name__ == '__main__':
    unittest.main()
