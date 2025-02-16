# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/merge-two-sorted-lists/
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.

        :param list1: The head node of the first sorted linked list of length 0 to 50.
        :param list2: The head node of the second sorted linked list of length 0 to 50.
        :returns: A single, sorted linked combining 'list1' and 'list2'.
        """
        # Make a dummy node to start the new merged list.
        mergedHead = ListNode()
        # Initialize a pointer to the end of the new merged list.
        curMerged = mergedHead
        # Initialize pointers along the two linked lists.
        curList1 = list1
        curList2 = list2
        # Loop while one of the pointers points to a node.
        while curList1 or curList2:
            # If the first list is out of nodes, the second list must have a node.
            if not curList1:
                # Add the node in the second linked list to the merged list and update each of the pointers.
                curMerged.next = curList2
                curMerged = curMerged.next
                curList2 = curList2.next
            # Otherwise, if the second list is out of nodes, the first list must have a node.
            elif not curList2:
                # Add the node in the first linked list to the merged list and update each of the pointers.
                curMerged.next = curList1
                curMerged = curMerged.next
                curList1 = curList1.next
            # Since both lists have nodes, add the node from the list that has the lower value to the merged list, and update each of the pointers.
            elif curList1.val < curList2.val:
                curMerged.next = curList1
                curMerged = curMerged.next
                curList1 = curList1.next
            else:
                curMerged.next = curList2
                curMerged = curMerged.next
                curList2 = curList2.next
        # Return the merged list, minus the dummy node made placed at the head.
        return mergedHead.next
