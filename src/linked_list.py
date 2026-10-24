#1.顺序表操作
class SeqList:
    def __init__(self, MAXSIZE=100):
        '''初始化顺序表'''
        self.MAXSIZE = MAXSIZE  # 顺序表的最大容量
        self.length = 0  # 顺序表的长度
        self.data = [None] * self.MAXSIZE  # 用于存储顺序表元素的列表




    def increase_length(self, increase_length):
        '''增加动态数组的长度'''
        new_length = self.length + increase_length# 最新的容量为当前容量加上增加的容量
        if new_length <= self.MAXSIZE:
            return  # 如果新的容量小于等于当前容量，则不需要增加
        new_data = [None] * new_length  # 创建一个新的列表用于存储
        for i in range(self.length):   #时间复杂度为O(n)
            new_data[i] = self.data[i]  # 将原来的数据复制到新的列表中
        self.data = new_data  # 更新数据列表为新的列表
        self.MAXSIZE = new_length  # 更新最大容量



    def list_insert(self, i, e)->bool:
        '''在顺序表的指定位置插入元素'''
        if i < 0 or i > self.length:
            return False  # 如果索引不合法，则返回False
        if self.length >= self.MAXSIZE:
            return False  # 如果顺序表已满，则返回False
        for j in range(self.length, i, -1):    #时间复杂度为O(n)
            self.data[j] = self.data[j - 1]  # 将元素向后移动
        self.data[i] = e  # 插入新元素
        self.length += 1  # 更新长度
        return True



    def list_delete(self, i)->bool:
        '''删除顺序表的指定位置的元素'''
        if i < 0 or i >= self.length:
            return False  # 如果索引不合法，则返回False
        data = self.data[i]  # 获取要删除的元素
        for j in range(i, self.length - 1):   #时间复杂度为O(n)
            self.data[j] = self.data[j + 1]  # 将元素向前移动
        self.data[self.length - 1] = None  # 清空最后一个元素
        self.length -= 1  # 更新长度
        return True


    def get_ele(self, i):
        '''获取顺序表的指定位置的元素'''
        if i < 0 or i >= self.length: #时间复杂度为O(1)
            return None  # 如果索引不合法，则返回None
        return self.data[i]  # 返回指定位置的元素


    def locate_ele(self, e):
        '''查找顺序表中指定元素的位序'''
        for i in range(self.length):  #时间复杂度为O(n)
            if self.data[i] == e:
                return i+1  #数组下标为i的元素与e相等，返回其位序i+1
        return 0  # 如果未找到，则返回0

#2.单链表操作
class LNode:
    def __init__(self, data=None):
        '''初始化链表节点'''
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        '''初始化链表(带头结点)'''
        self.head = LNode(None)  # 链表的头节点

    def list_insert(self, i, e)->bool:
        '''在链表的指定位置插入元素'''
        p=self.get_node(i-1) # 获取插入位置的前一个节点
        return self.insert_next(p, e)  # 在p节点后插入新节点


    def insert_next(self, p, e)->bool:
        '''在链表的指定节点后插入元素'''
        if p is None:
            return False  # 如果p为None，则返回False
        s = LNode(e)  # 创建新节点
        s.next = p.next  # 将新节点的next指向p的下一个节点
        p.next = s  # 将p的next指向新节点
        return True

    def insert_prior(self, p, s)->bool:
        '''在链表的指定节点前插入元素'''
        if p is None or s is None:
            return False  # 如果p或s为None，则返回False
        s.next = p.next  # 将新节点的next指向p的下一个节点
        p.next = s  # 将p的next指向新节点
        p.data, s.data = s.data, p.data  # 交换p和s的数据
        return True

    def list_delete(self, i)->bool:
        '''删除链表的指定位置的元素'''
        p=self.get_node(i-1) # 获取要删除的节点的前一个节点
        if p is None or p.next is None:
            return False  # 指针p为None或p的下一个节点为None，说明i值不合法，返回False
        q = p.next  # 获取要删除的节点
        p.next = q.next  # 将p的next指向q的下一个节点
        return True

    def delete_node(self, p)->bool:
        '''删除链表的指定节点'''
        if p is None:     #存在问题：如果p是最后一个节点，无法删除。只能通过遍历链表找到p的前一个节点，然后删除p
            return False  # 如果p为None，则返回False
        q = p.next  # 获取要删除的节点
        if q is None:
            return False  # 如果q为None，说明p是最后一个节点，无法删除，返回False
        p.data = q.data  # 将q的数据赋值给p
        p.next = q.next  # 将p的next指向q的下一个节点
        return True




    def get_node(self, i):
        '''获取链表的指定位置的节点'''
        if i < 0:
            return None  # 如果i值不合法，则返回None
        p = self.head  # 从头节点开始遍历
        j = 0
        while p is not None and j < i:  # 找到第i个节点
            p = p.next
            j += 1
        if p is None:
            return None  # 如果p为None，说明i值不合法，返回None
        return p  # 返回第i个节点


    def get_ele(self, i):
        '''获取链表的指定位置的元素'''
        node = self.get_node(i)# 获取第i个节点
        return node.data if node is not None else None  # 返回第i个节点的数据，如果节点不存在则返回None


    def locate_ele_node(self, e)->bool:
        '''查找链表中指定元素的节点'''
        p = self.head.next  # 从第一个节点开始遍历
        while p is not None and p.data != e:  # 遍历链表
            p = p.next
            if p is None:
                return None  # 如果遍历到链表末尾仍未找到指定元素，则返回None
        return p  # 如果找到指定元素，则返回其节点


    def create_tail(self, n):
        '''尾插法创建链表(顺序)'''
        r = self.head  # r指向尾节点，初始时指向头节点
        for i in range(n):
            s = LNode(i)  # 创建新节点
            r.next = s  # 将尾节点的next指向新节点
            r = s  # 将r指向新节点，成为新的尾节点
        r.next = None # 将尾节点的next指向None，表示链表结束
        return self

    def create_head(self, n):
        '''头插法创建链表(逆序)'''
        L = self.head  # L指向头节点
        L.next = None # 将头节点的next指向None，表示链表为空
        for i in range(n):
            s = LNode(i)  # 创建新节点
            s.next = L.next  # 将新节点的next指向头节点的下一个节点
            L.next = s  # 将头节点的next指向新节点
        return self

    # 反转链表 实质上是指针的反转，时间复杂度为O(n)，空间复杂度为O(1)
    def reverse(self):
        '''反转链表（非递归，单链表就地逆置）'''
        p = self.head.next  # p指向第一个节点
        pre = None  # pre指向前一个节点，初始时为None
        while p :  # 遍历链表
            next_node = p.next  # 保存下一个节点
            p.next = pre  # 将当前节点的next指向前一个节点，实现反转
            pre = p  # 将pre指向当前节点
            p = next_node  # 将p指向下一个节点
        self.head.next = pre  # 将头节点的next指向新的第一个节点



#3.双链表操作
class DNode:
    def __init__(self, data=None):
        '''初始化双链表节点'''
        self.data = data
        self.next = None
        self.prior = None

class DLinkedList:
    def __init__(self):
        '''初始化双链表(带头结点)'''
        self.head = DNode(None)  # 双链表的头节点
        self.head.next = None
        self.head.prior = None

    def list_insert(self, p: DNode, s: DNode)->bool:
        '''在p节点后插入新节点s'''
        if p is None or s is None:
            return False
        s.next = p.next
        if p.next is not None:
            p.next.prior = s
        s.prior = p
        p.next = s
        return True


    def delete_next(self, p: DNode)->bool:
        '''删除p节点的后继节点'''
        if p is None:
            return False
        q = p.next
        if q is None:
            return False
        p.next = q.next
        if q.next is not None:
            q.next.prior = p
        return True

#4.循环链表操作
class CNode:
    def __init__(self, data=None):
        '''初始化循环链表节点'''
        self.data = data
        self.next = None

class CLinkedList:
    def __init__(self):
        '''初始化循环链表(带头结点)'''
        self.head = CNode(None)  # 循环链表的头节点
        self.head.next = self.head  # 头节点的next指向自己，形成循环

#5.静态链表操作
class StaticNode:
    def __init__(self, data=None):
        '''初始化静态链表节点'''
        self.data = data
        self.next = 0
class SLinklist:
    def __init__(self, MAXSIZE=100):
        '''初始化静态链表'''
        self.MAXSIZE = MAXSIZE  # 静态链表的最大容量
        self.data = [StaticNode() for _ in range(MAXSIZE)]  # 用于存储静态链表节点的列表
        self.head = 0  # 静态链表的头节点下标
        self.free = 1  # 静态链表的空闲节点下标
        for i in range(1, MAXSIZE - 1):
            self.data[i].next = i + 1  # 将空闲节点连接起来
        self.data[MAXSIZE - 1].next = 0  # 最后一个空闲节点的next指向0，表示没有空闲节点

    def malloc(self)->int:
        '''分配一个空闲节点'''
        if self.free == 0:
            return 0  # 如果没有空闲节点，则返回0
        i = self.free  # 获取空闲节点下标
        self.free = self.data[i].next  # 更新空闲节点下标为下一个空闲节点
        return i  # 返回分配的空闲节点下标

    def free_node(self, i:int)->bool:
        '''释放一个节点'''
        if i <= 0 or i >= self.MAXSIZE:
            return False  # 如果i值不合法，则返回False
        self.data[i].next = self.free  # 将释放的节点的next指向当前空闲节点
        self.free = i  # 更新空闲节点下标为释放的节点
        return True

