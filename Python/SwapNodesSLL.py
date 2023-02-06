from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,head)
        prev = dummy
        current = head

        while current and current.next:
            # swap pointers
            prev.next = current.next
            current.next = prev.next.next
            prev.next.next = current
            # shift down one
            prev = current
            current = current.next

        return dummy.next

# test cases
if __name__ == "__main__":
    # create linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    # print linked list
    current = head
    print("Original: ")
    while current:
        print(current.val)
        current = current.next

    # swap nodes
    head = Solution().swapPairs(head)

    # print linked list
    current = head
    print("Swapped: ")
    while current:
        print(current.val)
        current = current.next