# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using two pointers
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next 
            # if they meet cycle exists
            if fast == slow :
                # To find cycle start 
                # move slow pointer to head
                slow=head
                while fast != slow:
                    # move both pointer one step at a time
                    slow=slow.next
                    fast=fast.next
                    # again meet point  is start of cycle
                return slow
        return None
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
    cycle=sol.detectCycle(node1)
    print(f"Cycle start at node {cycle.val}")



        