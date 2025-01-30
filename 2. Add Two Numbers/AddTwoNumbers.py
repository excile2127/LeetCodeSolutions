# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/add-two-numbers/
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two non-empty linked lists representing two non-negative integers with digits stored in reverse order.

        :param l1: The first linked list to sum.
        :param l2: The second linked list to sum.
        :returns: The sum of l1 and l2 as a linked list with digits stored in reverse order.
        """
        # Create new references for l1 and l2 in order to not change the parameter objects.
        curL1 = l1
        curL2 = l2
        # Create a dummy head for the sum linked list and set it as the current node in the sum.
        sumHead = ListNode()
        lastSumNode = sumHead
        # Initialize a flag determining whether the last sum had to carry over a digit.
        carryOver = False
        # Iterate over each linked list at the same time, stopping only once both lists have ran out of digits.
        while curL1 != None or curL2 != None:
            # Determine the value of each current node, if they exist. Use 0 if one of the lists has ran out of digits.
            l1Value = 0
            l2Value = 0
            if curL1 != None:
                l1Value = curL1.val
            if curL2 != None:
                l2Value = curL2.val
            # Sum the two values.
            sumValue = l1Value + l2Value
            # Check if the last sum had to carry over a digit
            if carryOver:
                # If so, increase the sum of these values by one and reset the carry over flag.
                sumValue += 1
                carryOver = False
            # Check if the value of this sum is more than a single digit.
            if sumValue > 9:
                # Remove the extra digit from this sum and signal the next sum to be increased by one.
                sumValue -= 10
                carryOver = True
            # Create a new node in the sum linked list with the determined value.
            sumNode = ListNode(sumValue)
            # Add the new node to the sum linked list and increment our pointer to it.
            lastSumNode.next = sumNode
            lastSumNode = sumNode
            # Increment the pointers for each linked list, handling if one of the lists has ran out of digits.
            if curL1 != None:
                curL1 = curL1.next
            if curL2 != None:
                curL2 = curL2.next
        # After iterating through all digits of both lists, check if there is still a digit left to carry over.
        if carryOver:
            # Create an extra node with a value of one and append it to the sum linked list.
            lastSumNode.next = ListNode(1)
        # Pop the dummy head off of the sum linked list, before returning it as the solution.
        return sumHead.next
