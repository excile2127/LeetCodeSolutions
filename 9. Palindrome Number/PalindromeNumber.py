import math
class Solution:
    # https://leetcode.com/problems/palindrome-number/
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether an integer is a palindrome without converting the integer to a string.

        :param x: A 32-bit signed integer.
        :returns: Whether x is a palindrome.
        """
        # Handle edge cases where x is negative (not a palindrome) or 0 (is a palindrome).
        if x < 0:
            return False
        if x == 0:
            return True
        # Find the number of digits within the input by using log10.
        numDigits = int(math.log10(x)) + 1
        # Initialize an empty list to contain individual digits of the input number.
        digits = []
        # Iterate over each digit in the input number.
        for i in range(numDigits):
            # Find the current digit by dividing by a scaling multiple of 10, then using modulus to only take the last digit.
            digit = x // (10 ** i)
            digit = digit % 10
            # Append this digit to the digits list.
            digits.append(digit)
            # Note that this will append the digits in inverse order. However, since palindromes are symmetrical, this does not matter.
        # Iterate over the digits on both sides, from the outside going in.
        for i in range(numDigits // 2):
            # If the digit on the left is not equal to the digit on the right, this number is not a palindrome.
            if digits[i] != digits[numDigits - i - 1]:
                return False
        # Since every digit had an equivalent pair on the other side of the number, the input number was a palindrome.
        return True
