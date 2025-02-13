class Solution:
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Finds all letter combinations from a phone number using recursion.

        :param digits: The digits of up to a 4 digit phone number, not including '1'.
        :returns: All letter combinations that could be made from 'digits'.
        """
        # Find the number of digits in the phone number.
        numDigits = len(digits)
        # If there are no digits, there are no letter combinations.
        if numDigits == 0:
            return []
        # Define a table of the letters that represent each digit.
        numToLetters = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        # Find the last digit in the phone number.
        lastDigit = digits[-1]
        # If it is the only digit, the letter combinations are simply its table entry.
        if numDigits == 1:
            return numToLetters[lastDigit]
        # Otherwise, find all letter combinations of the phone number without the last digit.
        combinations = self.letterCombinations(digits[:-1])
        # Iterate over the possible letters for the last digit and append them to every letter combination from the rest of the phone number.
        results = []
        for letter in numToLetters[lastDigit]:
            for combination in combinations:
                results.append(combination + letter)
        # Return the generated letter combinations.
        return results
