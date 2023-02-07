# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_sll(self, head: Optional[ListNode]) -> str:
        output = '['
        current = head
        while current:
            output += str(current.val) + ', '
            current = current.next
        output = output[0:len(output)-2]
        output += ']'
        return output

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        # check if next val is val, then repoint current.next to skip next node
        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        # adjust for head val since it was skiped
        if head.val == val:
            head = head.next
        
        return head

# test cases
if __name__ == "__main__":
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    # print & check linked list #1
    output = Solution().print_sll(head)
    removeElements = Solution().removeElements(head, 6)
    print(f'#1 Test: {output}')
    print(f'Removed list: {Solution().print_sll(removeElements)}')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #2
    head = None

    # print & check linked list #2
    removeElements = Solution().removeElements(head, 1)
    print(f'#2 Test: {head}')
    print(f'Removed list: [{Solution().print_sll(removeElements)}')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #3
    head = ListNode(7)
    head.next = ListNode(7)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(7)

    # print & check linked list #3
    output = Solution().print_sll(head)
    removeElements = Solution().removeElements(head, 7)
    print(f'#3 Test: {output}')
    print(f'Removed list: {Solution().print_sll(removeElements)}')