# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    if head == None or head.next == None:
        return
    ListNode newNode  = reverseList(head.next)
    
