# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        mid=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(mid)

        
        dummy=ListNode(0)
        curr=dummy

        while left and right:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        curr.next=left or right
        return dummy.next


        
