from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        visited = set()
        pointer = head

        while (pointer):
            if pointer in visited:
                return True
            else:
                visited.add(pointer)
            pointer = pointer.next

        return False

# test cases
if __name__ == "__main__":
    # create linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    # check if cycle
    hasCycle = Solution().hasCycle(head)
    print("Has Cycle: ", hasCycle)