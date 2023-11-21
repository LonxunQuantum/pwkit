import unittest

# python3 -m pwkit.ui.test.test_main_ui
from ..main_ui import MainUI


class MainUITest(unittest.TestCase):
    def test_show(self):
        main_ui = MainUI()
        main_ui.show()
        main_ui.process_int()
        
        
if __name__ == "__main__":
    unittest.main()