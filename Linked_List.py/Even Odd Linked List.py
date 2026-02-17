# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if linked list is empty
        if head is not None or  head.next is not None:
            return head
        # change links of odd and even nodes
        odd=head
        even_head=head.next
        even = head.next
        while even  and even.next :
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        # link last odd node with even node
        odd.next=even_head
        return head
if __name__ =="__main__":
    sol=Solution()
    node1 = ListNode(3) 
    node2 = ListNode(2) 
    node3 = ListNode(0) 
    node4 = ListNode(-4) 
    node1.next = node2 
    node2.next = node3 
    node3.next = node4
    node4.next = node2 
    res=sol.oddEvenList(node1)
    print(res.val)


        
      



        