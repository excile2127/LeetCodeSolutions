class Solution:
    # https://leetcode.com/problems/zigzag-conversion/
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern read line by line with a specified number of rows.

        :param s: A string with length between 1 and 1000 consisting of only English letters, ',', and '.'.
        :param numRows: The number of rows in a zigzag pattern, between 1 and 1000.
        """
        # If there is only 1 row in the zigzag pattern, simply return the original string.
        if numRows == 1:
            return s
        # Initialize an empty string to house the results of the convertion.
        result = ""
        # Initialize the current index of the zigzag pattern.
        curIndex = 0
        # Find the average offset between each letter in each row.
        totalOffset = 2 * (numRows - 1)
        # Start by using the first of the two possible offsets.
        firstOffset = True
        # Start with the first offset equal to the average offset and the second offset equal to 0.
        offset1 = totalOffset
        offset2 = 0
        # Store the length of the string for future use.
        strLen = len(s)
        # Initialize the base index to use whenever the current index resets to the beginning of a new line.
        baseIndex = 0
        # Iterate a number of times equal to the length of the string.
        for i in range(len(s)):
            # Append the character at the current index to the result string.
            result += s[curIndex]
            # If either offset is equal to the total offset, add the total offset to the current index.
            if offset1 == totalOffset or offset1 == 0:
                curIndex += totalOffset
            # If the first offset is marked, add the first offset to the current index and use the second offset on the next iteration.
            elif firstOffset:
                curIndex += offset1
                firstOffset = False
            # Otherwise, add the second offset to the current index and use the first offset on the next iteration.
            else:
                curIndex += offset2
                firstOffset = True
            # Check if the current index is out of bounds of the length of the string.
            if curIndex >= strLen:
                # Increment the base index and reset the current index to it.
                baseIndex += 1
                curIndex = baseIndex
                # Forcibly mark the first offset to be used.
                firstOffset = True
                # Decrease the first offset by 2 and increase the second offset by 2.
                offset1 -= 2
                offset2 += 2
        # Return the calculated result.
        return result
