class Solution:
    # https://leetcode.com/problems/3sum/
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all triplets of integers that sum to 0 in a list. Exceeds the time limit on large data sets.
        
        :param nums: A list of integers between -10^5 and 10^5 with a length between 3 and 3000.
        :returns: All triplets of integers that sum to 0 in 'nums'.
        """
        # Initialize a list of all unique pairs of numbers with their complement encountered in the list.
        complementPairs = {}
        # Initialize a list of all unique numbers encountered in the list
        seenNums = {}
        # Initialize a list of all solutions determined so far.
        results = set()
        # Iterate through all of the numbers in the input.
        for num in nums:
            # If this number has been seen 3 or more times before, skip it as it cannot make any more unique pairs.
            if num in seenNums and seenNums[num] > 2:
                continue
            # Check if the number has a pair that complements it.
            if num in complementPairs:
                # Iterate over all complements of the number.
                for pair in complementPairs[num]:
                    # Convert the solution of the 3 numbers to a sorted string (for it to be hashable).
                    result = " ".join(str(x) for x in sorted([num, pair[0], pair[1]]))
                    # Store the solution as a result if it is unique.
                    if result not in results:
                        results.add(result)
            # Iterate over all numbers seen before.
            for seenNum in seenNums:
                # Determine the complement of the current number and the a number seen before.
                complementNum = -1 * (num + seenNum)
                # If the complement doesn't have other results, initialize an empty list for the complement's pairs.
                if complementNum not in complementPairs:
                    complementPairs[complementNum] = []
                # Convert the pair of the current number and previously seen number into a sorted list.
                pair = sorted([num, seenNum])
                # If the pair hasn't been encountered before, store it as a pair under its complement.
                if pair not in complementPairs[complementNum]:
                    complementPairs[complementNum].append(pair)
            # If the number has not been seen before, add it to the list of seen numbers.
            if num not in seenNums:
                seenNums[num] = 0
            # Increment the number of times this number has been seen.
            seenNums[num] += 1
        # Convert the results from a list of strings to a list of string lists.
        results = [strResult.split() for strResult in results]
        # Convert the results from a list of string lists to a list of integer lists.
        results = [[int(strNum) for strNum in result] for result in results]
        # Return the results.
        return results
