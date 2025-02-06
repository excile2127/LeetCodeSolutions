class Solution:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Determines the length of the longest substring without repeating characters.

        :param s: A string up to length 5 * 10^4 only consisting of English letters, digits, symbols and spaces.
        :returns: The length of the longest substring without repeating characters.
        """
        # Initialize an empty dictionary that will contain letters seen in the current substring with their last-seen index.
        seenLetters = {}
        # Initialize the starting index of the current substring.
        startIndex = 0
        # Initialize the end index of the current substring, otherwise known as the index of the current letter.
        endIndex = 0
        # Initialize the maximum length found of a substring without repeating characters.
        maxLength = 0
        # Iterate over each letter in the string
        for letter in s:
            # Check if the letter has been seen in the current substring.
            if letter in seenLetters:
                # If it has, check if the length of the current substring without the new letter is longer than the maximum length of a substring found so far.
                if endIndex - startIndex > maxLength:
                    # If it has, update the max length to the length of the current substring without the new letter.
                    maxLength = endIndex - startIndex
                # Find the index the current letter was last seen at.
                lastSeenIndex = seenLetters[letter]
                # From the starting index of the current substring, iterate over the string until after the current letter was last seen.
                while startIndex != lastSeenIndex + 1:
                    # Remove the last-seen record of each letter encountered and update the starting index of the substring.
                    del seenLetters[s[startIndex]]
                    startIndex += 1
            # Regardless of whether the current letter was seen in the current substring, store the index it was found at in the seen letters dictionary and update the end index.
            seenLetters[letter] = endIndex
            endIndex += 1
        # After iterating over each letter in the string, check if the final substring was the longest substring.
        if endIndex - startIndex > maxLength:
            # If it was, update max length accordingly.
            maxLength = endIndex - startIndex
        # Return the maximum length found of a substring without repeating characters.
        return maxLength
