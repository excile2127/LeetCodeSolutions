class Solution:
    # https://leetcode.com/problems/median-of-two-sorted-arrays/
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays by merging the two arrays then finding the median. Runs in O(m+n) time.

        :param nums1: The first sorted array.
        :param nums2: The second sorted array.
        :returns: The median of nums1 and nums2.
        """
        # Find the total length of the two arrays combined.
        totalLength = len(nums1) + len(nums2)
        # Initialize left-most pointers for each array.
        p1 = 0
        p2 = 0
        # Create an empty array to house nums1 and nums2 being merged.
        mergedArray = []
        # Iterate over the total number of elements.
        for i in range(totalLength):
            # Check if the first array has already been fully iterated over.
            if p1 >= len(nums1):
                # Append the rest of the second array to the merged array before breaking, as there isn't any comparison left to do.
                mergedArray.extend(nums2[p2:])
                break
            # Check if the second array has already been fully iterated over.
            elif p2 >= len(nums2):
                # Append the rest of the first array to the merged array before breaking, as there isn't any comparison left to do.
                mergedArray.extend(nums1[p1:])
                break
            # Check if the number at the pointer in the first array is less than the number at the pointer in the second array.
            elif nums1[p1] < nums2[p2]:
                # Append the number at the pointer in the first array to the merged array, then move the first array pointer to the right.
                mergedArray.append(nums1[p1])
                p1 += 1
            else:
                # Append the number at the pointer in the second array to the merged array, then move the second array pointer to the right.
                mergedArray.append(nums2[p2])
                p2 += 1
        # Find the midpoint of the merged array by dividing by 2 and rounding down.
        midpoint = totalLength // 2
        # Check if the lenght of the merged array is odd.
        if totalLength % 2 == 1:
            # Return the median by returning the number in the merged array at the midpoint.
            return mergedArray[midpoint]
        # Return the median by returning the average of the two numbers around the midpoint in the merged array.
        return (mergedArray[midpoint] + mergedArray[midpoint - 1]) / 2
