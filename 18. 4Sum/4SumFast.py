class Solution:
    # https://leetcode.com/problems/4sum/
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all combinations of 4 numbers in a list that sum to a target value.

        :param nums: A list of integers  of length 1 to 200 with values between -10^9 amd 10^9.
        :param target: The value each combination of 4 number should sum to.
        :returns: All combinations of 4 numbers in 'nums' that sum to the 'target'.
        """
        # Find the number of integers in the input.
        n = len(nums)
        # If there are less than 4 numbers, it is impossible to have any combations of 4 numbers.
        if n < 4:
            return []
        # Sort the list.
        sortedList = sorted(nums)
        # Store results in a set.
        results = set()
        print (sortedList)
        # Iterate over the input, excluding the last 3 numbers.
        for i in range(n-3):
            # Fix this number as the first of the numbers in a possible combination.
            num1 = sortedList[i]
            # No more combinations can be found if the smallest sum is greater than the target.
            if num1 + sortedList[i+1] + sortedList[i+2] + sortedList[i+3] > target:
                break
            # No more combinations can be found with this number if the greatest sum is less than the target.
            if num1 + sortedList[n-1] + sortedList[n-2] + sortedList[n-3] < target:
                continue
            # Iterate over the input after the first number, excluding the last 2 numbers.
            for j in range(i+1,n-2):
                # Fix this number as the second of the numbers in a possible combination.
                num2 = sortedList[j]
                # Find the sum of the 2 fixed numbers.
                sum2 = num1 + num2
                # No more combinations can be found with the first number if the smallest sum is greater than the target.
                if sum2 + sortedList[j+1] + sortedList[j+2] > target:
                    break
                # No more combinations can be found with this number if the greatest sum is less than the target.
                if sum2 + sortedList[n-1] + sortedList[n-2] < target:
                    continue
                # Initialize a left pointer after the second fixed number and a right pointer at the end of the input.
                left = j+1
                right = n-1
                # Search for a possible solution while the left pointer hasn't crossed the right pointer.
                while left < right:
                    # Find the sum of the 2 fixed numbers and the numbers at the left and right pointer.
                    sum4 = sum2 + sortedList[left] + sortedList[right]
                    # If the sum is the target, a combination has been found.
                    if sum4 == target:
                        # Add the combination to the results set.
                        results.add((num1, num2, sortedList[left], sortedList[right]))
                        # Move both pointers inward, as both numbers must be different for a new distinct solution.
                        left += 1
                        right -= 1
                    # Otherwise, if the sum is under the target, increment the left pointer to increase the sum.
                    elif sum4 < target:
                        left += 1
                    # Since the sum is over the target, decrement the right pointer to decrease the sum.
                    else:
                        right -= 1
                    # If the number at a previous pointer was the same as the number at a current pointer, continue moving the pointer to find a new value.
                    if sum4 <= target:
                        while left < right and sortedList[left] == sortedList[left-1]:
                            left += 1
                    if sum4 >= target:
                        while right > left and sortedList[right] == sortedList[right+1]:
                            right -= 1
                    
        # Return all the combinations found.
        return list(results)
