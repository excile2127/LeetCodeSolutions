# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a linked list and returns its head.

        :param head: The head of a linked list with 1 to 30 nodes.
        :param n: The index from the end of the linked list used to remove the node.
        """
        # Add a dummy head node at the beginning of the list to handle edge cases.
        dummyHead = ListNode(next=head)
        # Initialize two pointers to nodes, a forward pointer and a back pointer.
        forward = dummyHead
        back = dummyHead
        # Move the forward pointer n nodes ahead of the back pointer.
        for _ in range(n):
            forward = forward.next
        # Move both the forward pointer and the back pointer ahead until the forward pointer reaches the end of the linked list.
        while forward.next:
            forward = forward.next
            back = back.next
        # Since the back pointer is now just before the node to remove, remove it.
        back.next = back.next.next
        # Return the original head of the linked list.
        return dummyHead.next
