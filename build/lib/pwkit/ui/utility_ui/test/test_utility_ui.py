import unittest

# python3 -m pwkit.ui.utility_ui.test.test_utility_ui
from ..utility_ui import UtilityUI


class UtilityUITest(unittest.TestCase):
    def test_show(self):
        UtilityUI().show()
        
        
        
if __name__ == "__main__":
    unittest.main()