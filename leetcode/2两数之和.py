
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        results = ListNode()
        p = results

        while l1 and l2:

            sub_sum = l1.val + l2.val  # ! 中间过程的值

            #! 当前节点的值，要加上这个节点本来的值和位置数
            p.val = p.val + sub_sum
            sub_ = p.val  # ! 在计算最后一位时候使用的标志位，在计算中间过程时候不起作用
            front = p.val // 10  # ! 表示进位标志
            p.val = p.val % 10  # ! 表示这个节点位置填的数

            #! 进位
            if front == 0:
                p.next = ListNode()
            elif front != 0:
                p.next = ListNode(front)

            #! 当两位数长度不一致的时候判断需要在哪个数添加节点
            #! 当两位数长度一致时候判断时候有进位存在
            if l1.next == None and l2.next == None:
                if sub_ // 10 != 0:
                    p.next = ListNode(1)
                else:
                    p.next = None
            elif l1.next == None and l2.next != None:
                l1.next = ListNode()
            elif l1.next != None and l2.next == None:
                l2.next = ListNode()

            p = p.next
            l1 = l1.next
            l2 = l2.next

        return results
