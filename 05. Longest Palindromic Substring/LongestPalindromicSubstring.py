class Solution:
  # https://leetcode.com/problems/longest-palindromic-substring/
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindrome within a string using a simplified Manacher's Algorithm.

        :param s: A string with length between 1 and 1000 using only digits and English letters.
        :returns: The longest palindromic substring in s.
        """
        # Store the length of the longest known palindrome.
        maxLen = 1
        # Initialize the longest known palindrome to be the first character.
        maxPalindrome = s[0]
        # If the input is only one character, it is the longest palindrome in the input string.a
        if len(s) == 1:
            return maxPalindrome
        # Insert extra non-valid characters between each character in the input string to turn any string with an even number of characters into a string with an odd number of characters.
        s = '#' + '#'.join(s) + '#'
        # Store the length of the modified input string.
        strLen = len(s)
        # Iterate over each character in the modified input string.
        for i in range(strLen):
            # Expand from the current character as the center character in a possible palindrome.
            for j in range(i):
                # Find the lower and upper bound of the possible palindrome.
                lower = i - j - 1
                upper = i + j + 1
                # If the upper bound is out of bounds, move on to the next center character.
                if upper >= strLen:
                    break
                # Check if the lower and upper character of the possible palindrome match.
                if s[lower] == s[upper]:
                    # Since the lower and upper characters match, this string is a palindrome.
                    palindrome = s[lower:upper+1]
                    # If the length of this palindrome is greater than the length of the longest found palindrome so far, update it as the solution.
                    palindromeLen = len(palindrome)
                    if palindromeLen > maxLen:
                        maxLen = palindromeLen
                        maxPalindrome = palindrome
                    # Continue expanding around this center character, as it is so far a palindrome.
                    continue
                # Since the lower and upper character do not match, this string and any string with it as a center cannot be a palindrome, so move on to the next center character.
                else:
                    break
        # Remove all added characters from the solution.
        maxPalindrome = maxPalindrome.replace('#', '')
        # Return the longest found palindrome.
        return maxPalindrome
