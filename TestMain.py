import unittest
import sys

sys.path.append("src")

from Twin import *
from SizeError import *

class TestTwin(unittest.TestCase):
    val_ok="Yes"
    val_notok="No"
    
    def test_simple_Yes(self):
        self.assertEqual(Twin.twins(['abcde'],['adebc']), [TestTwin.val_ok])
        
    def test_simple_No(self):
        self.assertEqual(Twin.twins(['abcde'],['adebe']), [TestTwin.val_notok])
        
    def test(self):
        self.assertEqual(Twin.twins(['abcde','aa','bcd'],['adebc','ab','dcb']), [TestTwin.val_ok,TestTwin.val_notok,TestTwin.val_ok])
        
    def test_nonstr(self):
        """
        lists with non string
        """
        with self.assertRaises(Exception): Twin.twins([1],['aa'])
        
    def test_diffsizes(self):
        """
        lists of different sizes
        """
        with self.assertRaises(Exception): Twin.twins(['abcde'],['adeb','aa'])
        
unittest.main(argv=[''], verbosity=2, exit=False)
