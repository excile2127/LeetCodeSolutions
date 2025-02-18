# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/swap-nodes-in-pairs/
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps every two adjacent nodes in a linked list without changing the values of the list's nodes.

        :param head: The head of the original linked list of size 0 to 100.
        :returns: The head of the new linked list.
        """
        # Initialize the first node to swap in the first pair.
        first = head
        # If the list is empty, return an empty head.
        if not first:
            return first 
        # Initialize the second node to swap in the first pair
        second = head.next
        # If the list only contains one element, return that element as the head without modification.
        if not second:
            return first
        # Store the new head of the linked list, as well as the last element in the list before the current swap.
        newHead = second
        last = None
        # Loop while there are two nodes to swap.
        while first and second:
            # Update the next pointer of the last node swapped to reflect the new swap.
            if last:
                last.next = second
            # Swap the first and the second nodes in the current pair.
            first.next = second.next
            second.next = first
            # Update the last node swapped to reflect the swap that just occured.
            last = first
            # Update the first and second node pointers for the next loop.
            first = first.next
            if first:
                second = first.next
        # Return the new head of the swapped linked list.
        return newHead
