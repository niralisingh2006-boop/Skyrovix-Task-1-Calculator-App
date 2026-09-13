import unittest
from calculator.app import Calculator
class T(unittest.TestCase):
 def setUp(self): self.c=Calculator()
 def test_math(self): self.assertEqual(self.c.calculate(2,'+',3),5); self.assertEqual(self.c.calculate(8,'-',3),5); self.assertEqual(self.c.calculate(4,'*',3),12); self.assertEqual(self.c.calculate(10,'/',2),5)
 def test_zero(self):
  with self.assertRaises(ZeroDivisionError): self.c.calculate(1,'/',0)
 def test_history(self): self.c.calculate(2,'+',2); self.assertEqual(len(self.c.history),1); self.c.clear_history(); self.assertEqual(len(self.c.history),0)
