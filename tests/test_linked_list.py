"""
第2章 线性表 单元测试
覆盖：顺序表、单链表、双链表、循环链表、静态链表

运行方式：
    pytest tests/test_linked_list.py -v
    或：python tests/test_linked_list.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from linked_list import (
    SeqList,
    LNode,
    LinkedList,
    DNode,
    DLinkedList,
    CLinkedList,
    SLinklist,
)


# ---------- 顺序表 ----------

class TestSeqList:
    def test_init(self):
        '''测试顺序表的初始化'''
        sl = SeqList(5)
        assert sl.length == 0
        assert len(sl.data) == 5

    def test_append_and_insert(self):
        '''测试顺序表的追加和插入操作'''
        sl = SeqList(10)
        sl.list_insert(0, 10)
        sl.list_insert(1, 20)
        sl.list_insert(2, 30)
        assert sl.data[:3] == [10, 20, 30]
        assert sl.length == 3

    def test_insert_at_head(self):
        '''测试在顺序表头部插入元素'''
        sl = SeqList(10)
        for e in [10, 20, 30]:
            sl.list_insert(sl.length, e)
        assert sl.list_insert(0, 99)
        assert sl.data[:4] == [99, 10, 20, 30]

    def test_insert_mid(self):
        '''测试在顺序表中间插入元素'''
        sl = SeqList(10)
        for e in [10, 20, 30]:
            sl.list_insert(sl.length, e)
        assert sl.list_insert(1, 55)
        assert sl.data[:4] == [10, 55, 20, 30]

    def test_insert_full_returns_false(self):
        '''测试在顺序表已满时插入元素返回False'''
        sl = SeqList(3)
        for e in [1, 2, 3]:
            assert sl.list_insert(sl.length, e)
        assert sl.list_insert(0, 99) is False  # 已满

    def test_insert_invalid_index(self):
        '''测试在顺序表中插入元素时，索引不合法返回False'''
        sl = SeqList(3)
        assert sl.list_insert(5, 1) is False
        assert sl.list_insert(-1, 1) is False

    def test_delete(self):
        '''测试顺序表的删除操作'''
        sl = SeqList(10)
        for e in [10, 20, 30, 40]:
            sl.list_insert(sl.length, e)
        assert sl.list_delete(1)
        assert sl.data[:3] == [10, 30, 40]
        assert sl.length == 3

    def test_delete_invalid_index(self):
        '''测试在顺序表中删除元素时，索引不合法返回False'''
        sl = SeqList(10)
        sl.list_insert(0, 1)
        assert sl.list_delete(1) is False
        assert sl.list_delete(-1) is False

    def test_get_ele(self):
        '''测试获取顺序表中指定位置的元素'''
        sl = SeqList(10)
        for e in [10, 20, 30]:
            sl.list_insert(sl.length, e)
        assert sl.get_ele(0) == 10
        assert sl.get_ele(2) == 30
        assert sl.get_ele(3) is None

    def test_locate_ele(self):
        '''测试查找顺序表中指定元素的位序'''
        sl = SeqList(10)
        for e in [10, 20, 30]:
            sl.list_insert(sl.length, e)
        assert sl.locate_ele(10) == 1  # 返回位序（1 基）
        assert sl.locate_ele(30) == 3
        assert sl.locate_ele(999) == 0  # 未找到返回 0

    def test_increase_length(self):
        '''测试顺序表的扩容操作'''
        sl = SeqList(3)
        for e in [1, 2, 3]:
            sl.list_insert(sl.length, e)
        sl.increase_length(2)  # 扩容到 5
        assert sl.MAXSIZE == 5
        assert sl.list_insert(3, 4)

# ---------- 单链表 ----------

class TestLinkedList:
    def test_create_tail(self):
        '''测试尾插法创建链表'''
        ll = LinkedList()
        ll.create_tail(5)  # 0,1,2,3,4
        assert list(ll) == [0, 1, 2, 3, 4]

    def test_create_head(self):
        '''测试头插法创建链表'''
        ll = LinkedList()
        ll.create_head(4)  # 3,2,1,0
        assert list(ll) == [3, 2, 1, 0]

    def test_list_insert(self):
        '''测试在链表的指定位置插入元素'''
        ll = LinkedList()
        ll.create_tail(3)  # 0,1,2
        assert ll.list_insert(1, 99) is True
        assert list(ll) == [99, 0, 1, 2]
        assert ll.list_insert(3, 77) is True
        assert list(ll) == [99, 0, 77, 1, 2]

    def test_list_insert_invalid(self):
        '''测试在链表的指定位置插入元素时，索引不合法返回False'''
        ll = LinkedList()
        ll.create_tail(2)
        assert ll.list_insert(0, 1) is False   # i<1 非法（约定：位序从 1 开始）
        assert ll.list_insert(99, 1) is False  # 超出表长
        assert ll.list_insert(-1, 1) is False  # i<1 非法

    def test_list_delete(self):
        '''测试删除链表的指定位置的元素'''
        ll = LinkedList()
        ll.create_tail(4)  # 0,1,2,3
        assert ll.list_delete(1) is True
        assert list(ll) == [1, 2, 3]
        assert ll.list_delete(3) is True
        assert list(ll) == [1, 2]

    def test_list_delete_invalid(self):
        '''测试删除链表的指定位置的元素时，索引不合法返回False'''
        ll = LinkedList()
        ll.create_tail(2)
        assert ll.list_delete(0) is False
        assert ll.list_delete(3) is False
        assert ll.list_delete(-1) is False

    def test_get_ele(self):
        '''测试获取链表的指定位置的元素'''
        ll = LinkedList()
        ll.create_tail(3)
        assert ll.get_ele(1) == 0
        assert ll.get_ele(3) == 2
        assert ll.get_ele(4) is None
        assert ll.get_ele(-1) is None

    def test_locate_ele_node(self):
        '''测试查找链表中指定元素的节点'''
        ll = LinkedList()
        ll.create_tail(5)  # 0,1,2,3,4
        node = ll.locate_ele_node(3)
        assert node is not None and node.data == 3
        assert ll.locate_ele_node(999) is None

    def test_insert_next_and_insert_prior(self):
        '''测试在链表的指定节点后插入元素和前插元素'''
        ll = LinkedList()
        ll.create_tail(2)  # 0,1
        head = ll.head
        assert ll.insert_next(head, 5)
        assert list(ll) == [5, 0, 1]
        first = ll.head.next
        s = LNode(7)
        assert ll.insert_prior(first, s)  # 交换法前插
        assert list(ll) == [7, 5, 0, 1]

    def test_delete_node(self):
        '''测试复制删除法删除链表的指定节点'''
        ll = LinkedList()
        ll.create_tail(3)  # 0,1,2
        node = ll.get_node(2)  # 节点 1
        assert ll.delete_node(node)  # 复制删除法：用后继覆盖
        assert list(ll) == [0, 2]

    def test_delete_node_tail_returns_false(self):
        '''测试复制删除法删除链表的尾节点返回False'''
        ll = LinkedList()
        ll.create_tail(2)
        tail = ll.get_node(2)
        assert ll.delete_node(tail) is False  # 尾节点无法用复制法删除

    def test_reverse(self):
        '''测试链表的反转操作'''
        ll = LinkedList()
        ll.create_tail(5)  # 0,1,2,3,4
        ll.reverse()
        assert list(ll) == [4, 3, 2, 1, 0]
        ll.reverse()  # 反转两次还原
        assert list(ll) == [0, 1, 2, 3, 4]

    def test_reverse_single_and_empty(self):
        '''测试链表的反转操作在空表和单节点表的情况'''
        ll = LinkedList()
        ll.reverse()  # 空表不崩
        assert list(ll) == []
        ll.create_tail(1)
        ll.reverse()  # 单节点不变
        assert list(ll) == [0]

    def test_iter(self):
        '''测试 __iter__：链表可转列表、可 for 循环、可求和'''
        ll = LinkedList()
        ll.create_tail(5)  # 0,1,2,3,4
        assert list(ll) == [0, 1, 2, 3, 4]
        assert sum(x for x in ll) == 10

    def test_len(self):
        '''测试 __len__：空表为 0，随插删变化'''
        ll = LinkedList()
        assert len(ll) == 0
        ll.create_tail(3)
        assert len(ll) == 3
        ll.list_delete(1)
        assert len(ll) == 2

    def test_repr(self):
        '''测试 __repr__：字符串表示与空表'''
        ll = LinkedList()
        ll.create_tail(3)
        assert repr(ll) == '0->1->2'
        assert repr(LinkedList()) == ''

# ---------- 双链表 ----------

class TestDLinkedList:
    def _make(self, n):
        """辅助：用连续插入造 0..n-1 的双链表"""
        dll = DLinkedList()
        r = dll.head
        for i in range(n):
            dll.list_insert(r, DNode(i))
            r = r.next
        return dll

    def test_insert(self):
        '''测试在双链表的指定节点后插入新节点'''
        dll = self._make(3)  # 0,1,2
        # 校验双向链接
        p = dll.head.next
        assert p.data == 0 and p.prior is dll.head
        p = p.next.next
        assert p.data == 2 and p.prior.data == 1 and p.next is None

    def test_delete_next(self):
        '''测试删除双链表的指定节点的后继节点'''
        dll = self._make(3)  # 0,1,2
        head = dll.head
        assert dll.delete_next(head)  # 删 0 -> [1,2]
        p = dll.head.next
        assert p.data == 1 and p.prior is dll.head
        assert dll.delete_next(p)  # 删 2 -> [1]
        assert dll.head.next.data == 1 and dll.head.next.next is None

    def test_delete_next_none(self):
        '''测试删除双链表的指定节点的后继节点时，若后继节点为None返回False'''
        dll = self._make(1)
        p = dll.head.next
        assert dll.delete_next(p) is False

# ---------- 循环链表 ----------

class TestCLinkedList:
    def test_init_self_loop(self):
        '''测试循环链表的初始化，头结点的next指向自身'''
        cll = CLinkedList()
        assert cll.head.next is cll.head

# ---------- 静态链表 ----------

class TestSLinklist:
    def test_malloc_and_free(self):
        '''测试静态链表的分配和释放节点'''
        sl = SLinklist(5)
        i1 = sl.malloc()
        i2 = sl.malloc()
        assert (i1, i2) == (1, 2)
        assert sl.free == 3

    def test_free_node_reuse(self):
        '''测试释放节点后，下次分配复用它'''
        sl = SLinklist(5)
        i1 = sl.malloc()
        assert sl.free_node(i1)
        assert sl.free == i1  # 释放的节点回到空闲链头部
        assert sl.malloc() == i1  # 下次分配复用它

    def test_malloc_exhausted(self):
        '''测试静态链表的分配节点耗尽时返回0'''
        sl = SLinklist(3)
        sl.malloc()
        sl.malloc()
        assert sl.malloc() == 0  # 空闲链耗尽返回 0

    def test_free_node_invalid(self):
        '''测试释放节点时，若下标不合法返回False'''
        sl = SLinklist(3)
        assert sl.free_node(0) is False
        assert sl.free_node(3) is False

if __name__ == "__main__":
    # 无 pytest 环境时直接运行
    for name, cls in list(globals().items()):
        if name.startswith("Test"):
            for attr in dir(cls):
                if attr.startswith("test_"):
                    inst = cls()
                    getattr(inst, attr)()
                    print(f"PASS {name}.{attr}")
    print("All tests passed!")
