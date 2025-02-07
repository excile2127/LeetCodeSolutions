import math
class Solution:
    # https://leetcode.com/problems/integer-to-roman/
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to its Roman numeral equivalent.

        :param num: An integer between 1 and 3999.
        :returns: The Roman numeral equivalent of num as a string.
        """
        # Initialize a table of integer values to their Roman numeral equivalent.
        romanTable = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        # Get the values of each Roman numeral in descending order.
        romanValuesDescOrder = sorted(romanTable.keys(), reverse=True)
        # Initialize a variable to hold the result of this function.
        result = ""
        # Execute until num is 0.
        while num > 0:
            # Find the number of digits after the first digit in num.
            numDigitsAfterFirst = int(math.log10(num))
            # Find the first digit in num.
            firstDigit = num // (10 ** numDigitsAfterFirst)
            # Check if the first digit is a 4 or a 9 (to use subtractive form).
            if firstDigit == 4 or firstDigit == 9:
                # Find two values of the subtractive form.
                firstSub = 10 ** numDigitsAfterFirst
                secondSub = (firstDigit + 1) * (10 ** numDigitsAfterFirst)
                # Append both Roman numeral equivalents of the values to the result.
                result += romanTable[firstSub]
                result += romanTable[secondSub]
                # Decrease num by the net sum of the subtractive form value.
                num -= secondSub - firstSub
                # Move on to the next loop.
                continue
            # Since the first digit isn't a 4 or a 9, iterate over the values of each Roman numeral in descending order.
            for romanValue in romanValuesDescOrder:
                # Check if the value could be in num.
                if num >= romanValue:
                    # Append the Roman numeral equivalent of the value to the result.
                    result += romanTable[romanValue]
                    # Decrease num by the value.
                    num -= romanValue
                    # Move on to the next loop.
                    break
        # Return the calculated result.
        return result
            
