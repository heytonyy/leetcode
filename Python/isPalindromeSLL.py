# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # edge case
        if not head:
            return False

        # find mid point and determine if even
        counter = 0
        current = head
        while current:
            counter += 1
            current = current.next
        mid = int(counter/2)
        even = True if counter % 2 == 0 else False
        
        # set the pointers (left side will be reversed)
        counter = 0
        current = head
        while not counter == mid:
            counter += 1
            current = current.next
        left_pointer = head
        right_pointer = current

        # reverse left side
        prev = None
        current = left_pointer
        next = left_pointer
        while not current == right_pointer:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        # check if right and left are the same
        curr_left = prev
        curr_right = right_pointer if even else right_pointer.next


        while curr_left:
            if not curr_left.val == curr_right.val:
                return False
            curr_left = curr_left.next
            curr_right = curr_right.next
        

        return True
    
    def print_sll(self, head: Optional[ListNode]) -> str:
        output = '['
        current = head
        while current:
            output += str(current.val) + ', '
            current = current.next
        output = output[0:len(output)-2]
        output += ']'
        return output

# test cases
if __name__ == "__main__":
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)

    # print & check linked list #1
    output = Solution().print_sll(head)
    isPalindrome = Solution().isPalindrome(head)
    print(f'#1 Test: {output} --- Is Palindrome?: {isPalindrome}')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)

    # print & check linked list #2
    output = Solution().print_sll(head)
    isPalindrome = Solution().isPalindrome(head)
    print(f'#2 Test: {output} --- Is Palindrome?: {isPalindrome}')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create linked list #3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    # print & check linked list #1
    output = Solution().print_sll(head)
    isPalindrome = Solution().isPalindrome(head)
    print(f'#3 Test: {output} --- Is Palindrome?: {isPalindrome}')
