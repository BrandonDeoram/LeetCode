"""
:type head: ListNode
:rtype: ListNode
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    

    return 1


head = [1, 2, 3, 4, 5]

print(reverseList(ListNode(head)))
