import unittest

# python3 -m pwkit.ui.generator_ui.test.test_generator_ui
from ..generator_ui import GeneratorUI


class GeneratorUITest(unittest.TestCase):
    def test_show(self):
        GeneratorUI().show()
        
        

if __name__ == "__main__":
    unittest.main()