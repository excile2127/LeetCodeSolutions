class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Finds the sum of three integers in a list of integers that is closest to a target value.

        :param nums: A list of integers with values between -1000 and 1000 of length 3 to 500.
        :param target: The target value that the sum of three integers should be closest to with a value between -10^4 and 10^4.
        :returns: The sum of three integers in 'nums' that is closest to the 'target'.
        """
        # Sort the input in ascending order.
        nums = sorted(nums)
        # Store the sum of three numbers found that is closest to the target.
        closestSum = float('inf')
        # Store the distance from the closest sum to the target value.
        closestDistance = float('inf')
        # Iterate over each number in the input, fixing it as a possible number in the the closest triplet.
        for i, fixed in enumerate(nums):
            # Initialize a left and right pointer at the left and right bounds of remaining input.
            left = i + 1
            right = len(nums) - 1
            # Search for the closest input until the left pointer crosses the right pointer.
            while left < right:
                # Find the current sum using the fixed number and the numbers at the left and right pointers.
                curSum = nums[i] + nums[left] + nums[right]
                # Calculate the distance away from the target the current sum is.
                curDistance = abs(curSum - target)
                # Check if current sum is closer to the target than the previous closest sum.
                if curDistance < closestDistance:
                    # If the target is the same as the current sum, then there is no need to keep searching.
                    if curDistance == 0:
                        return target
                    # Update the closest sum and its distance from the target.
                    closestSum = curSum
                    closestDistance = curDistance
                # If the current sum is less than the target, increment the left pointer to increase the current sum.
                if curSum < target:
                    left += 1
                # Otherwise, decrement the right pointer to decrease the current sum.
                else:
                    right -= 1
        # Return the closest sum found.
        return closestSum
