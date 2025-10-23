import unittest
from unittest.mock import patch  #replaces user input to test the function
from datetime import date, timedelta  #calculates duration between dates
import duration_calender  #pull the code from the file I am unit testing

class TestDuration(unittest.TestCase):

    @patch('builtins.input', return_value=(date.today() - timedelta(days=3)).strftime("%Y-%m-%d"))
    def test_duration_runs(self, mock_input):
        """This test checks if the duration() function runs without crashing."""
        duration_calender.duration()
       

if __name__ == '__main__':
    unittest.main()
    #unit test complete
    print("unit test complete")
    
