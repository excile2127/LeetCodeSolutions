class Solution:
    # https://leetcode.com/problems/container-with-most-water/
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum area between two heights in a graph.

        :param height: A list of heights on a graph with 2 to 2 * 10^5 elements of up to size 10^4.
        :returns: The maximum area between two heights within 'height'.
        """
        # Initialize a left and right pointer at the beginning and end of the list of heights.
        leftP = 0
        rightP = len(height) - 1
        # Initialize a variable to store the highest area found between two heights.
        curMaxArea = 0
        # Execute until the left pointer is greater than or equal to the right pointer.
        while leftP < rightP:
            # Find the heights at the current pointer positions.
            leftH = height[leftP]
            rightH = height[rightP]
            # Find the area between the two heights.
            curArea = min(leftH, rightH) * (rightP - leftP)
            # If this area is highest than the highest area found so far, this is the next maximum area.
            if curArea > curMaxArea:
                curMaxArea = curArea
            # Check if the left height is lower than the right height.
            if leftH < rightH:
                # Since the left height is lower, move the left pointer to the right, as this has the highest possibility of increased area.
                leftP += 1
            else:
                # Other, the right height is lower or equal to the left height, so move the right pointer to the right for the same reason.
                rightP -= 1
        # Return the maximum area found between two heights.
        return curMaxArea
