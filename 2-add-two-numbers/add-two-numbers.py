# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        carry=0
        dummy=ListNode(0)
        head=dummy

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            carry,curr_val=divmod(val1+val2+carry,10)
            head.next=ListNode(curr_val)
            head=head.next

            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0

        return dummy.next
