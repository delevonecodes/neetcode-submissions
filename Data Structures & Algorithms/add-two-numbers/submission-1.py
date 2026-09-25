# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, head2 = l1, l2
        num1, num2 = [], []
        
        while head or head2:
            if head:
                num1.insert(0, head.val)
                head = head.next
            if head2:
                num2.insert(0, head2.val)
                head2 = head2.next
            
        num1 = int("".join(map(str, num1)))
        num2 = int("".join(map(str, num2)))
        total = list(str(num1+num2))
        total = total[::-1]
        new_list = dummy = ListNode()
        for i, num in enumerate(total):
            dummy.val = num
            dummy.next = ListNode() if i < len(total)-1 else None
            dummy = dummy.next
            
        return new_list

        
        
            