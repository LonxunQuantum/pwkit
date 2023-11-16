import unittest

# python3 -m pwkit.ui.module_ui.test.test_module_ui
from ..module_ui import ModuleUI


class ModuleUITest(unittest.TestCase):
    def test_show(self):
        ModuleUI().show()
        
        
if __name__ == "__main__":
    unittest.main()