class Solution:
    # https://leetcode.com/problems/roman-to-integer/
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral to its integer representation.

        :param s: A valid Roman numeral with a length between 1 and 15.
        :returns: The integer representation of 's'.
        """
        # Define the value of each Roman numeral.
        romanTable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # Initialize a variable to store the converted value of the input.
        result = 0
        # Initialzie a variable to store the last calculated value of a Roman numeral.
        lastValue = float('inf')
        # Iterate over each Roman numeral in the input.
        for numeral in s:
            # Find the value of the Roman numeral.
            # Since the input is guarranteed to be a valid Roman numeral, no need to check if its a valid numeral.
            value = romanTable[numeral]
            # Check if the value of this numeral is greater than the value of the last Roman numeral.
            if value > lastValue:
                # If it is, the last value should have been subtracted rather than added, so decrease the result by twice the last value.
                result -= lastValue * 2
            # Add the value of the Roman numeral to the result.
            result += value
            # Store the value of this Roman numeral for the next iteration.
            lastValue = value
        # Return the converted result.
        return result
