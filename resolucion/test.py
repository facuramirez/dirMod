from ejercicio import resolucion
import unittest

class TestVerifyExercise(unittest.TestCase):
    def test1(self):
        resultado1 = resolucion('hi')
        self.assertEqual(resultado1, '44 444')
    
    def test2(self):
        resultado2 = resolucion('yes')
        self.assertEqual(resultado2, '999337777')
    
    def test3(self):
        resultado1 = resolucion('foo bar')
        self.assertEqual(resultado1, '333666 666022 2777')
    
    def test4(self):
        resultado4 = resolucion('hello world')
        self.assertEqual(resultado4, '4433555 555666096667775553')

if __name__ == '__main__':
    unittest.main()
