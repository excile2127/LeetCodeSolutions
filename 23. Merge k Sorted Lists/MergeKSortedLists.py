# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/merge-k-sorted-lists/
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges up to 10^4 sorted linked-lists together into a single sorted linked-list.

        :param lists: Between 0 and 10^4 head nodes of sorted linkedlists with up to 500 elements each.
        :returns: A single linked-list combining all lists in 'lists'.
        """
        # 
        numLists = len(lists)
        # 
        if numLists == 0:
            return None
        # 
        elif numLists == 1:
            return lists[0]
        # 
        firstHalfMerged = self.mergeKLists(lists[:numLists//2])
        secondHalfMerged = self.mergeKLists(lists[numLists//2:])
        # 
        return self.merge2Lists(firstHalfMerged, secondHalfMerged)
        
    def merge2Lists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges two, sorted linked-lists into one sorted linked-list.

        :param list1: The first sorted linked list's head with 0 to 500 elements.
        :param list2: The second sorted linked list's head with 0 to 500 elements.
        :returns: The lists of 'list1' and 'list2' combined into a single, sorted linked-list.
        """
        # Initialize and store a refernce a dummy head node for the merged linked-list, as well as the current end of the list.
        mergedHead = ListNode()
        curMerged = mergedHead
        # Loop while both list1 and list2 have elements.
        while list1 and list2:
            # Add the smaller value of list1 and list2 to the end of the merged linked-list and move respective pointers forward.
            if list1.val < list2.val:
                curMerged.next = list1
                list1 = list1.next
            else:
                curMerged.next = list2
                list2 = list2.next
            curMerged = curMerged.next
        # If either list1 or list2 has elements remaining, add the entire list to the end of the merged linked-list.
        if list1:
            curMerged.next = list1
        elif list2:
            curMerged.next = list2
        # Return the merged linked-list.
        return mergedHead.next
