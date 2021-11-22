from main import add
import unittest

class AddTest(unittest.TestCase):
    def setUp(self):
        self.x1 = 2
        self.x2 = 3
        
        self.y1 = -2
        self.y2 = 0
        
        self.z1 = 0
        self.z2 = 3
        
    def test_add1(self):
        self.assertEqual(add(self.x1, self.y1), self.z1)
    
    def test_add2(self):
        self.assertEqual(add(self.x2, self.y2), self.z2)

if __name__ == '__main__':
    unittest.main()
        
