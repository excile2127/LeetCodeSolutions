class Solution:
    # https://leetcode.com/problems/two-sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers in a list that sum to a target.

        :param nums: A list of numbers containing exactly one solution.
        :param target: The sum the two solution numbers will add up to.
        :returns: The indices of the solution numbers.
        """
        # Create an empty hash map that will store possible solutions as the key and the index of their complement as the value.
        hashMap = {}
        # Keep track of the current index when iterating over nums.
        i = 0
        # Iterate over nums once.
        for num in nums:
            # Check to see if the complement of the current number is stored in the hash map.
            if num in hashMap:
                # If it is, return the index stored in the hash map and the current index as the solution.
                return [hashMap[num], i]
            # Otherwise, determine the complement of the current number...
            complement = target - num
            # And store the current index at with the complement as the key in the hash map.
            hashMap[complement] = i
            # Lastly, increment the index.
            i += 1
        # By the problem definition, this should never be hit, as a solution is guaranteed.
        return []
