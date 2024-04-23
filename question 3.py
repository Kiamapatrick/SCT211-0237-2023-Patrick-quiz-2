class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
