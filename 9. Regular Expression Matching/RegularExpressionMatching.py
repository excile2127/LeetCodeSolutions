class Solution:
    # https://leetcode.com/problems/regular-expression-matching/
    def isMatch(self, s: str, p: str) -> bool:
        """
        Determines whether an input string matches a regular expression pattern with support for '.' and '*". Uses backtracking and dynamic programming.

        :param s: An input string consisting of only lowercase English letters with a length between 1 and 20.
        :param p: A regular expression pattern consisting of only lowercase English letters, '.', and '*' with a length between 1 and 20.
        :returns: Whether the input string s matches the regular expression pattern p.
        """
        # Define a dynamic programming dictionary that will store whether a pairing of an input and pattern match.
        dp = {}

        def isMatchDP(s: str, p: str, dp: dict) -> bool:
            """
            Helper function for isMatch that includes a dynamic programming dictionary.

            :param s: Same as isMatch.
            :param p: Same as isMatch.
            :param dp: A dynamic programming dictionary that stores whether a pairing of an input and a pattern match.
            :returns: Same as isMatch.
            """
            # Handle base case where both the input and pattern are empty.
            if not s and not p:
                # All characters have been successfully consumed, so the input and pattern match.
                return True
            # Handle base case where there is input remaining, but the pattern is empty.
            if not p:
                # All characters have not been successfully consumed, so the input and pattern do not match.
                return False
            # Check if this string and pattern have already been checked on if they match.
            sAndP = (s, p)
            if sAndP in dp:
                # If it has, return the previous result.
                return dp[sAndP]
            # Find the last character in the pattern.
            lastPChar = p[-1]
            # Handle case where the last character is a star (matches one or more characters).
            if lastPChar == '*':
                # Determine if the input matches the pattern without the starred character by calling this function again.
                matchedWithoutStar = isMatchDP(s, p[:-2], dp)
                # Handle edge case where there is no input remaining, but there is a pattern ending in a star.
                if not s:
                    # Since no input is remaining, the star must match 0 characters. Return the result of whether this input matches the pattern without the starred character.
                    return matchedWithoutStar
                # Check if the input matches the pattern without the starred character.
                if matchedWithoutStar:
                    # Since they match without the starred character, the input and the pattern match.
                    # Store this result in the dynamic programming dictionary and return it.
                    dp[sAndP] = matchedWithoutStar
                    return dp[sAndP]
                # Find the last character in the input and the character that has been starred.
                lastSChar = s[-1]
                starChar = p[-2]
                # Check if the starred character is a dot (can match anything), or if the last character in the input matches the starred character.
                if starChar == '.' or lastSChar == starChar:
                    # Since these characters match, this input could match the pattern if the rest of the input and pattern match.
                    # Call this function again without the last character in the input, but keep the starred character.
                    # Store this result in the dynamic programming dictionary and return it.
                    dp[sAndP] = isMatchDP(s[:-1], p, dp)
                    return dp[sAndP]
                # Since the last character of the input doesn't match the starred character, the input and the pattern do not match.
                # Store this result in the dynamic programming dictionary and return it.
                dp[(s, p)] = False
                return dp[(s, p)]
            # Handle base case where there is no input remaining, but there is a pattern remaining without a star.
            if not s:
                # There is pattern remaining without input that has to be matched, so the input and pattern do not match.
                return False
            # Find the last character in the input.
            lastSChar = s[-1]
            # Check if the last character in the pattern is a dot, or if the last character in the input and pattern match
            if lastPChar == '.' or lastSChar == lastPChar:
                # Since these characters match, this input could match the pattern if the rest of the input and pattern match.
                # Call this function again without the last characters in the input and pattern.
                # Store this result in the dynamic programming dictionary and return it.
                dp[(s, p)] = isMatchDP(s[:-1], p[:-1], dp)
                return dp[(s, p)]
            # Since the last characters of the input and pattern do not match, the input and pattern do not match.
            # Store this result in the dynamic programming dictionary and return it.
            dp[(s, p)] = False
            return dp[(s, p)]

        # Call the helper function defined above with the newly-created dynamic programming dictionary.
        return isMatchDP(s, p, dp)
