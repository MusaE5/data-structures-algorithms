# reverse_linked_list.py
# Problem: Reverse a singly linked list.
# logic is in the reverseList function.
# Everything else is just for testing and visualization.
# Use 3 pointers(one pointing at none (p), one at head, one at next link.)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ORIGINAL CODE 
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev
#  CODE ENDS HERE 🔼

# The rest is just for testing the function with an example

def build_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")

# Example usage
head = build_list([1, 2, 3, 4, 5])
print("Original List:")
print_list(head)

reversed_head = reverseList(head)
print("Reversed List:")
print_list(reversed_head)
