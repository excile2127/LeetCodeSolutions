class Solution:
    # https://leetcode.com/problems/reverse-integer/
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of an integer within a 32-bit integer range.

        :param x: A 32-bit iacnteger.
        :returns: x with the digits reversed if it would be within a 32-bit range. Otherwise, 0.
        """
        # Convert the input to a string.
        originalStr = str(x)
        # Determine whether the input was negative, and strip the '-' from its string representation if so.
        isNegative = False
        if originalStr[0] == '-':
            isNegative = True
            originalStr = originalStr[1:]
        # Reverse the digits of string input.
        reversedStr = ""
        for char in reversed(originalStr):
            reversedStr += char
        # Find the maximum absolute value the result can be.
        maxInt = 2 ** 31
        if not isNegative:
            maxInt -= 1
        # Convert this maximum absolute value to a string.
        maxStr = str(maxInt)
        # Find the length of the result and the maximum absolute value.
        reversedLen = len(reversedStr)
        maxLen = len(maxStr)
        # If the result would have more digits than the maximum absolute value, it is guaranteed to be greater, so return 0.
        if reversedLen > maxLen:
            return 0
        # If the result has the same number of digits as the maximum absolute value, it may be greater or less than, so check each digit.
        elif reversedLen == maxLen:
            # Iterate over both the result and maximum absolute value.
            for i in range(maxLen):
                # Find the digit of each string.
                reversedDigit = int(reversedStr[i])
                maxDigit = int(maxStr[i])
                # If the digit is greater, it the result is greater, so return 0.
                if reversedDigit > maxDigit:
                    return 0
                # If the digit is less than, then the result is less than, so finish checking early.
                elif reversedDigit < maxDigit:
                    break
                # Otherwise, the digit is the same, so check the next digit.
        # Reverse the validated result.
        reversedInt = int(reversedStr)
        # If the string was originally negative, make the result negative.
        if isNegative:
            reversedInt *= -1
        # Return the result.
        return reversedInt
