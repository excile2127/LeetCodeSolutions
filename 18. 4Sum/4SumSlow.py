class Solution:
    # https://leetcode.com/problems/4sum/
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all combinations of four numbers in a list that sum to a target value.

        :param nums: A list of integers with values between -10^9 amd 10^9 of length 1 to 200.
        :param target: The value all found combinations of four numbers should sum to.
        :returns: All combinations of four numbers in 'nums' that sum to the 'target'.
        """
        # Find the number of integers in the input.
        n = len(nums)
        # If there are less than 4 numbers, it is impossible to have any combations of 4 numbers.
        if n < 4:
            return []
        # Sort the list to optimize each loop.
        sortedList = sorted(nums)
        # Find the largest number, as well as the sum of the largest 2, 3, and 4 numbers.
        last = sortedList[-1]
        last2 = last + sortedList[-2]
        last3 = last2 + sortedList[-3]
        last4 = last3 + sortedList[-4]
        # If the sum of the largest 4 numbers is less than the target, no values in the input can sum to the target.
        if last4 < target:
            return []
        # Store combinations of four numbers in a set to guarrantee uniqueness.
        results = set()
        # Iterate over the input, except the last 3 numbers.
        for i in range(n-3):
            # Fix the number being iterated on.
            num1 = sortedList[i]
            # If this number plus the largest 3 numbers is less than the target, no combinations featuring this number can sum to the target.
            if num1 + last3 < target:
                continue
            # Iterate over the input after the first number, except the last 2 numbers.
            for j in range(i+1, n-2):
                # Fix the second number being iterated on.
                num2 = sortedList[j]
                # Find the sum of the 2 fixed numbers.
                sum2 = num1 + num2
                # If the sum of the first 2 numbers and the sum of the largest 2 numbers is less than the target, no combinations featuring these 2 numbers can sum to the target.
                if sum2 + last2 < target:
                    continue
                # Iterate over the input after the second number, except the last number.
                for k in range(j+1, n-1):
                    # Fix the third number being iterated on.
                    num3 = sortedList[k]
                    # Find the sum of the 3 fixed numbers.
                    sum3 = sum2 + num3
                    # Find what the 4th number must be.
                    num4 = target - sum3
                    # Check if the 4th number exists in the input after the 3rd number.
                    if num4 in sortedList[k+1:]:
                        # If it does, it and the 3 fixed numbers are a solution.
                        results.add((num1, num2, num3, num4))
        # Return all the combinations found.
        return list(results)
