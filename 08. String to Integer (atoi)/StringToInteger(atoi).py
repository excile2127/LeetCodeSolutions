class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to an integer.
        
        :param s: A string consisting of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
        :returns: The integer representation of s ignoring leading whitespace, maintaining sign, clamped to a 32-bit integer range, and ignoring all character after a non-numeric character.
        """
        # Remove all leading whitespace from the input string.
        s = s.lstrip(' ')
        # Ensure the string has input remaining after removing leading whitespace.
        if len(s) == 0:
            return 0
        # Determine if the string represents a positive or negative number and remove any sign from the input string.
        isNegative = False
        if s[0] == '+' or s[0] == '-':
            isNegative = s[0] == '-'
            # Ensure the string has input remaining after removing the sign.
            if len(s) == 1:
                return 0
            s = s[1:]
        # Remove all leading zeroes from the input string.
        s = s.lstrip('0')
        # Determine the absolute maximum value that can be converted from a string to an integer.
        absMax = 2 ** 31
        if not isNegative:
            absMax -= 1
        # Iterate over each character in the input string.
        result = 0
        for char in s:
            # Exit early if each if the current character is not a number.
            if not char.isnumeric():
                break
            # Multiply the current result by 10 to signify adding a digit.
            result *= 10
            # Convert the current character to a digit and add it to the result.
            digit = int(char)
            result += digit
            # Check if the current result is greater than the absolute maximum it can be.
            if result >= absMax:
                # Set the result to the absolute maximum and exit early.
                result = absMax
                break
        # If the result is supposed to be negative, make it negative.
        if isNegative:
            result *= -1
        # Return the result.
        return result
