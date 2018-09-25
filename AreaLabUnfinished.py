import math #lets us use the math module
import unittest # unittest module helps us test small sections of code

def circleArea(radius): 
    return radius*radius*math.pi

def rectArea(base, height):
    return base*height

def trapArea(base1, base2, height):
    return (base1 + base2)/2*height

def triArea(base,height):
    return (base*height)/2
    
	
class MyTest(unittest.TestCase): # using TestCase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
        self.assertAlmostEqual(circleArea(3.25), 33.1830724)
    def testRectArea(self):
        self.assertEqual(rectArea(5, 4), 20)
        self.assertEqual(rectArea(654, 564), 654*564)
    def testTrapArea(self):
        self.assertEqual(trapArea(5,5,4), (5 + 5)/2*4)
        self.assertEqual(trapArea(754,65,7), (754 + 65)/2*7)
    def testTriArea(self):
        self.assertEqual(triArea(5,4), 10)
        self.assertEqual(triArea(43,654), (43*654)/2)
    
    