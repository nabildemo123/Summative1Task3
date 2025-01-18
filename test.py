import unittest 
from main import fizzbuzz

class testfizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")


    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        
    def test_other(self):
        self.assertEqual(fizzbuzz(4), "4")




if __name__ == '__main__':
    unittest.main(exit = False)