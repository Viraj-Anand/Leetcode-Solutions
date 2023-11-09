# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def split(head):
            slow=head
            fast=head
            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next

            mid=slow.next
            slow.next=None
            return mid

        def rev(head):
            prev=None
            curr=head

            while curr:
                forw=curr.next
                curr.next=prev
                prev=curr
                curr=forw
            return prev

        def merge(l1,l2):
            dummy=ListNode(0)
            curr=dummy

            while l1 and l2:
                curr.next=l1
                l1=l1.next
                curr=curr.next
                curr.next=l2
                l2=l2.next
                curr=curr.next

            if l1:
                curr.next=l1
            if l2:
                curr.next=l2

            return dummy.next

        splitlist=split(head)
        revlist=rev(splitlist)
        return merge(head,revlist)
            




        