class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    if not head or not head.next:
        return None

    slow = head.next
    fast = head.next.next

    while slow != fast:
        if not fast or not fast.next:
            return None
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
