import unittest


from src.roman_converter import decimal_to_roman 
class TestRomanConverter(unittest.TestCase):
    
    def test_basic_numbers_1(self):
        self.assertEqual(decimal_to_roman(1), "I")
    def test_basic_numbers_5(self):
        self.assertEqual(decimal_to_roman(5), "V")
    def test_basic_numbers_10(self):
        self.assertEqual(decimal_to_roman(10), "X")
    def test_basic_numbers_50(self):
        self.assertEqual(decimal_to_roman(50), "L")
    def test_basic_numbers_100(self):
        self.assertEqual(decimal_to_roman(100), "C")
    def test_basic_numbers_500(self):
        self.assertEqual(decimal_to_roman(500), "D")
    def test_basic_numbers_1000(self):
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_subtraction_rules_4(self):
        self.assertEqual(decimal_to_roman(4), "IV")
    def test_subtraction_rules_9(self):
        self.assertEqual(decimal_to_roman(9), "IX")
    def test_subtraction_rules_40(self):
        self.assertEqual(decimal_to_roman(40), "XL")
    def test_subtraction_rules_90(self):
        self.assertEqual(decimal_to_roman(90), "XC")
    def test_subtraction_rules_400(self):
        self.assertEqual(decimal_to_roman(400), "CD")
    def test_subtraction_rules_900(self):
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex_numbers_49(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
    def test_complex_numbers_99(self):
        self.assertEqual(decimal_to_roman(99), "XCIX")
    def test_complex_numbers_499(self):
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
    def test_complex_numbers_999(self):
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
    def test_complex_numbers_3999(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()









#import unittest
#from roman_converter import decimal_to_roman

#class TestRomanConverter(unittest.TestCase):
#    def test_basic_numbers(self):
#        self.assertEqual(decimal_to_roman(1), "I")
#        self.assertEqual(decimal_to_roman(5), "V")
#        self.assertEqual(decimal_to_roman(10), "X")

#    def test_subtraction_rules(self):
#        self.assertEqual(decimal_to_roman(4), "IV")
#        self.assertEqual(decimal_to_roman(9), "IX")
#        self.assertEqual(decimal_to_roman(40), "XL")
#        self.assertEqual(decimal_to_roman(90), "XC")

#    def test_complex_numbers(self):
#        self.assertEqual(decimal_to_roman(49), "XLIX")
#        self.assertEqual(decimal_to_roman(99), "XCIX")
#        self.assertEqual(decimal_to_roman(499), "CDXCIX")
#        self.assertEqual(decimal_to_roman(999), "CMXCIX")
#        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

#if __name__ == '__main__':
#    unittest.main()