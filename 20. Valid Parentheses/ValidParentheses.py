class Solution:
    # https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        """
        Validates whether a string only has matching brackets.

        :param s: A string consisting only of '()[]{}' of length 1 to 10^4.
        """
        # Map each type of open and close bracket to each other.
        bracketMap = {'(': ')', '{': '}', '[': ']'}
        # Initialize a stack to put the open brackets into.
        stack = []
        # Iterate over the input.
        for char in s:
            # Check if the current character is an open bracket.
            if char in bracketMap:
                # If it is, add it to the stack.
                stack.append(char)
            # Otherwise, the current character is a closed bracket.
            else:
                # If the stack is empty, the closed bracket cannot match an open bracket, so return false early.
                if not stack:
                    return False
                # Otherwise, pop the last open bracket off the stack.
                lastOpen = stack.pop()
                # If the last open bracket doesn't match the type of closed bracket encountered, return false early.
                if char != bracketMap[lastOpen]:
                    return False
        # Since the entire string was parsed and matched, the string is valid if the stack is empty.
        return not stack
