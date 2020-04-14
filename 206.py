# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    if head.next is None or head is None:
        return head
    now = head
    temp = None
    while now is not None:
        now.next, temp, now = temp, now, now.next     
    return temp



Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
head = reverseList(Node1)

while(head is not None):
    print (head.val)
    head = head.next

