from numpy.polynomial.tests.test_laguerre import L3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# p = ListNode()
class LinkList:
    def __init__(self):
        self.head=None
        p = ListNode()

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r=self.head
        
        p = self.head
        
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
        
            p.next = ListNode(i)  # type: ignore
            p = p.next
        
        return r
    
    def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val,end='')
            node = node.next
            
    # 83. 删除排序链表中的重复元素
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
    
    # 21. 合并两个有序链表
    from typing import Optional ## Optional 是什么
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2  # 终止条件，直到两个链表都空
        if not list2: return list1
        if list1.val <= list2.val:  # 递归调用
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
    
    # 203. 移除链表元素
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head
    
    # 206. 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre
    
    # 234. 回文链表
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        print(vals)
        return vals == vals[::-1]
    
    # 237. 删除链表中的节点
    def deleteNode(self, node): ## 怎样传入 node

        node.val = node.next.val
        node.next = node.next.next

    # 876. 链表的中间结点 ## 快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def middleNode_1(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

    # 1290. 二进制链表转整数
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans
    
    # 剑指 Offer 06. 从尾到头打印链表
    from typing import List
    def reversePrint(self, head: ListNode) -> List[int]:
        # cur = head
        # A = []
        # while cur is not None :
        #     A.append(cur.val)
        #     cur = cur.next
        # A = A[::-1]
        # return A
        return self.reversePrint(head.next) + [head.val] if head else []
    
    # 剑指 Offer 25. 合并两个排序的链表
    
    def mergeTwoLists_Jianzhi_Offer(self, l1: ListNode, l2: ListNode) -> ListNode:
           
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

      
    
if __name__ == '__main__':
    l = LinkList()
    data1 = [1, 1,0,1]
    data2 = [2,3,6]
    l1=l.initList(data1)
    l2=l.initList(data2)
    l3=l.mergeTwoLists(l1,l2) # 怎样合并完不修改本链表
    l.printlist(l3)
    
    # a = l.getDecimalValue(l1)
    # print(a)
    # l.printlist(l1)
    # print("\n")
    # # l.deleteNode(l1,1)  # type: ignore
    # print("\n")
    # l1 = l.middleNode_1(l1)
    # l.printlist(l1)
    # print(data1[::-1])
    
    # l.removeElements(l3,2)  # type: ignore
    
    # l.printlist(l3)
    
    # l.printlist(l1)
    # print("\n")
    # l1=l.deleteDuplicates(l1)
    # l.printlist(l1)
    # print("\n")
    # l1 = l.reverseList(l1)
    # l.printlist(l1)


