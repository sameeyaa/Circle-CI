import unittest
from unittest.mock import patch
from datetime import date, timedelta
import io
import sys
import duration_calender

class TestDurationCalender(unittest.TestCase):

    @patch('builtins.input', return_value=(date.today() - timedelta(days=10)).strftime("%Y-%m-%d"))
    def test_duration_output(self, mock_input):
        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        duration_calender.duration()  # Run your original function

        sys.stdout = sys.__stdout__  # Reset stdout

        output = captured_output.getvalue()

        # Check that output includes expected text
        self.assertIn("Today's date:", output)
        self.assertIn("10 days", output or str(10))  # difference in days appears

    @patch('builtins.input', return_value='12-12-2020')
    def test_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            duration_calender.duration()

if __name__ == '__main__':
    unittest.main()
