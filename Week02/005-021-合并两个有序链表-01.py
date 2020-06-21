class ListNote:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    # 首先先创建一个将 列表转换成链表的函数
    def linkList(self, list):
        # 将列表的第一个元素初始化为头节点，避免 0 的多余
        headNote = ListNote(list[0])
        # 将节点值返回
        newList = headNote
        # 将列表中的其它元素，依次赋值到链表中
        for i in list[1:]:
            # 利用 for 循环，使节点依次指向列表中的元素
            headNote.next = ListNote(i)
            # 将节点依次后移，这样才能保证，链表中的元素在增加
            headNote = headNote.next
        return newList

    # 将两个有序链表合并，其实原理与将列表转换成链表类似
    def mergeTwoLists(self, l1, l2):
        # 初始化头节点，头节点为 0
        headNote = ListNote(0)
        # 返回节点值
        newLinkList = headNote
        while l1 and l2:
            if l1.val < l2.val:
                headNote.next = l1
                headNote = headNote.next
                l1 = l1.next
            else:
                headNote.next = l2
                headNote = headNote.next
                l2 = l2.next
        # 如果链表 l1 和 l2 还有剩余，则把剩下的都赋值给节点
        if l1 or l2:
            headNote.next = l1 or l2
        return newLinkList.next

list1 = [1, 2, 4]
list2 = [1, 3, 4]

t1 = Solution()
linkList1 = t1.linkList(list1)
linkList2 = t1.linkList(list2)

newLinkList = t1.mergeTwoLists(linkList1, linkList2)
print(newLinkList)
print(newLinkList.val)
