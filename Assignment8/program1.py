class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
    
    def to_roman(self, num):
        result = ""
        for value, symbol in self.roman_numerals.items():
            while num >= value:
                result += symbol
                num -= value
        return result
    
    def to_int(self, roman):
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and self._is_roman(roman[i]) and self._is_roman(roman[i+1]):
                result += self.roman_numerals[self._roman_to_int(roman[i:i+2])]
                i += 2
            else:
                result += self.roman_numerals[self._roman_to_int(roman[i])]
                i += 1
        return result
    
    def _is_roman(self, char):
        return char in ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    def _roman_to_int(self, roman):
        return self.roman_numerals[roman]