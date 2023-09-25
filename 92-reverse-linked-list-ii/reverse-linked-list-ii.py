# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head is None:
            return None

        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for _ in range(left-1):
            prev=prev.next

        curr=prev.next
        forw=curr.next

        for _ in range(right-left):
            curr.next=forw.next
            forw.next=prev.next
            prev.next=forw
            forw=curr.next

        return dummy.next