class Solution:
    # https://leetcode.com/problems/3sum/
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all triplets of integers that sum to 0 in a list.
        
        :param nums: A list of integers between -10^5 and 10^5 with a length between 3 and 3000.
        :returns: All triplets of integers that sum to 0 in 'nums'.
        """
        # Initialize new lists for all positive and negative numbers in the input, as well as the number of zeroes.
        posList = []
        zeros = 0
        negList = []
        # Populate the lists of all positive and negative numbers, and count the number of zeroes.
        for num in nums:
            if num > 0:
                posList.append(num)
            elif num == 0:
                zeros += 1
            else:
                negList.append(num)
        # Transform the lists of positive and negative numbers into sets for faster lookup time.
        posSet = set(posList)
        negSet = set(negList)
        # Generate a set to store all triplets that sum to zero.
        results = set()
        # If there are three or more zeroes, a triplet of three zeroes is a possible solution.
        if zeros >= 3:
            results.add((0, 0, 0))
        # If there is at least one zero, each pair of a positive and negative number that sums to zero is a possible solution.
        if zeros > 0:
            for posNum in posSet:
                complement = posNum * -1
                if complement in negSet:
                    results.add((complement, 0, posNum))
        # For every pair of positive numbers, there could be a negative number that is their complement as a possible solution.
        for i, posNum1 in enumerate(posList):
            for j in range(i+1, len(posList)):
                posNum2 = posList[j]
                complement = -1 * (posNum1 + posNum2)
                if complement in negSet:
                    results.add(tuple(sorted([complement, posNum1, posNum2])))
        # For every pair of negative numbers, there could be a positive number that is their complement as a possible solution.
        for i, negNum1 in enumerate(negList):
            for j in range(i+1, len(negList)):
                negNum2 = negList[j]
                complement = -1 * (negNum1 + negNum2)
                if complement in posSet:
                    results.add(tuple(sorted([negNum1, negNum2, complement])))
        # Return all found solutions.
        return list(results)
