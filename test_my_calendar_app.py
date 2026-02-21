import unittest
from my_calendar_app import find_day_of_week

class TestCalendarApp(unittest.TestCase):
    def test_find_day_of_week_valid(self):
        # Known dates
        self.assertEqual(find_day_of_week(2023, 10, 24), "Tuesday")
        self.assertEqual(find_day_of_week(2024, 2, 29), "Thursday")  # Leap year
        self.assertEqual(find_day_of_week(2021, 1, 1), "Friday")

    def test_find_day_of_week_invalid_date(self):
        # February 29th in a non-leap year
        self.assertIsNone(find_day_of_week(2023, 2, 29))

    def test_find_day_of_week_invalid_month(self):
        # Month 13
        self.assertIsNone(find_day_of_week(2023, 13, 1))
        # Month 0
        self.assertIsNone(find_day_of_week(2023, 0, 1))

    def test_find_day_of_week_invalid_day(self):
        # Day 32
        self.assertIsNone(find_day_of_week(2023, 1, 32))
        # Day 0
        self.assertIsNone(find_day_of_week(2023, 1, 0))

    def test_find_day_of_week_edge_cases(self):
        # Very high year
        self.assertEqual(find_day_of_week(9999, 12, 31), "Friday")
        # Negative year/day/month (datetime will raise ValueError)
        self.assertIsNone(find_day_of_week(-1, 1, 1))

if __name__ == '__main__':
    unittest.main()
