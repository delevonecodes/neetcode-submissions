# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        visited = []
        while curr:
            if not curr.next:
                return False
            elif curr in visited:
                return True
            else:
                visited.append(curr)
                curr = curr.next
                
            
