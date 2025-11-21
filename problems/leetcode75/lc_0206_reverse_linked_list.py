# Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)
# Difficulty: Easy
# Tags: Linked List, Recursion

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

def build_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def to_list(head: ListNode | None) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

solution = Solution()

test_cases = [
    ([1,2,3,4,5]), #[5,4,3,2,1]
    ([1,2]),       #[2,1]
    ([]),          #[]
]

for head in test_cases:
    print(to_list(solution.reverseList(build_linked_list(head))))
