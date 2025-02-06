class Solution:
    # https://leetcode.com/problems/median-of-two-sorted-arrays/
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays by using binary sort to create and validate partitions on the smaller array. Runs in O(log(n)) time.

        :param nums1: The first sorted array.
        :param nums2: The second sorted array.
        :returns: The median of nums1 and nums2.
        """
        # Find which array is the smaller of two in order to perform binary search on the smaller array for efficiency.
        # If both arrays are the same size, this step can be ignored.
        smaller = nums1
        larger = nums2
        if len(smaller) > len(larger):
            smaller = nums2
            larger = nums1
        # Find the lengths of each array and the total length of both arrays combined
        smallerLength = len(smaller)
        largerLength = len(larger)
        totalLength = smallerLength + largerLength
        # Find how large each partition (subarray on the left and right side of the median) would be if the arrays were merged.
        partitionSize = (totalLength + 1) // 2
        # Initialize the left and right pointers for binary search on the smaller array.
        leftSearchPointer = 0
        rightSearchPointer = smallerLength
        # Iterate until the problem is solved. This should effectively be a "while true", unless the arrays were not sorted.
        while leftSearchPointer <= rightSearchPointer:
            # Determine the size of the left partition that exists within the smaller array.
            smallerMidpoint = (leftSearchPointer + rightSearchPointer) // 2
            # Determine the size of the left partition that existsw within the larger array.
            largerMidpoint = partitionSize - smallerMidpoint
            # Initialize the values of the boundaries of each partition within each array.
            smallerLeft = float('-inf')
            smallerRight = float('inf')
            largerLeft = float('-inf')
            largerRight = float('inf')
            # If the left partition exists in each array, grab the highest value in it.
            if smallerMidpoint > 0:
                smallerLeft = smaller[smallerMidpoint - 1]
            if largerMidpoint > 0:
                largerLeft = larger[largerMidpoint - 1]
            # If the right partition exists in each array, grab the lowest value in it.
            if smallerMidpoint < smallerLength:
                smallerRight = smaller[smallerMidpoint]
            if largerMidpoint < largerLength:
                largerRight = larger[largerMidpoint]
            # If the highest value of each left partition is less than the lowest value of the opposite right partition, the problem is solved.
            if smallerLeft <= largerRight and largerLeft <= smallerRight:
                # Check if the total number of elements is odd.
                if totalLength % 2 == 1:
                    # If it is, find the median by grabbing the largest value from the left partition.
                    return max(smallerLeft, largerLeft)
                # If its even, average the largest value of the left partition with the lowest value of the right partition.
                return (max(smallerLeft, largerLeft) + min(smallerRight, largerRight)) / 2.0
            # Check if the highest value of the left partition in the smaller array is larger than the lowest value of the right partition in the higher array.
            elif smallerLeft > largerRight:
                # If it is, lower the right search pointer to be smaller than the mid point (halving the problem space).
                rightSearchPointer = smallerMidpoint - 1
            # Otherwise, the highest value of the left partition in the larger array must be larger than the lowest value of the right partition in the smaller array.
            else:
                # So, increase the left search pointer to be the higher than the mid point (also halving the problem space).
                leftSearchPointer = smallerMidpoint + 1
        # The function should return the median within the while loop. If it hasn't, at least one of the arrays wasn't sorted.
        return -1
