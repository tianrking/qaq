

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
            
    # @classmethod
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
    
if __name__ == '__main__':
    l = LinkList()
    data1 = [1, 1, 2, 3]
    l1=l.initList(data1)
    l.printlist(l1)
    print("\n")
    l1=l.deleteDuplicates(l1)
    l.printlist(l1)
    # print("\n")


