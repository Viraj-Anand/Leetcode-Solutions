# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow

        while curr:
            forw=curr.next
            curr.next=prev
            prev=curr
            curr=forw

        x=prev
        y=head
        while x:
            if x.val!=y.val:
                return False
            x=x.next
            y=y.next

        return True

        
        

        