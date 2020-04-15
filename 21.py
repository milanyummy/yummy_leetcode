#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    #迭代法
    # now = ListNode(-1)
    # head = now  
    # while l1 and l2:
    #     if l1.val <= l2.val:
    #         now.next = l1
    #         l1 = l1.next
    #     else:
    #         now.next = l2
    #         l2 = l2.next
    #     now = now.next
    # now.next = l1 if (l2 is None) else l2
    # head = head.next      
    # return head

    #递归法
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
    