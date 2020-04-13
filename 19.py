# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    #自写单趟扫描，list保存倒数n个链表节点
    # tempList = []
    # now = head
    # if head.next is None:
    #     return None
    # while now.next is not None:
    #     tempList.append(now)
    #     if len(tempList) > n:
    #         tempList.pop(0)
    #     now = now.next
    # tempList.append(now)
    # if n == len(tempList):
    #     head.next = tempList[1]
    #     return head
    # if n == 1:
    #     tempList[-2].next = None
    # else:
    #     tempList[0].next = tempList[2]
    # return head

    #快慢指针单趟扫描,增加初始节点规避极端情况
    if head.next is None:#链表节点少于等于一个
        return None
    startNode = ListNode(-1)
    startNode.next = head
    slow = fast = startNode
    for i in range(n):
        fast = fast.next
    if fast.next is None:
        return slow.next.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head


Node1 = ListNode(1)
Node2 = ListNode(2)
Node1.next = Node2