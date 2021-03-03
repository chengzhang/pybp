# 面试题 16.25. LRU 缓存
# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。
#
# 它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#


class Node(object):
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key2value = {}
        self.key2node = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.key2value:
            return -1
        self.move_to_head(key)
        return self.key2value[key]

    def put(self, key, value):
        if key in self.key2value:
            self.move_to_head(key)
        else:
            self.add_to_head(key)
            if len(self.key2value) >= self.capacity:
                removed_key = self.remove_tail()
                self.key2value.pop(removed_key)
        self.key2value[key] = value

    def move_to_head(self, key):
        node = self.key2node[key]
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        self._add_to_head(node)

    def add_to_head(self, key):
        node = Node(key)
        self.key2node[key] = node
        self._add_to_head(node)

    def _add_to_head(self, node):
        old_head = self.head.next
        self.head.next = node
        node.prev, node.next = self.head, old_head
        old_head.prev = node

    def remove_tail(self):
        old_tail = self.tail.prev
        left = old_tail.prev
        left.next = self.tail
        self.tail.prev = left
        self.key2node.pop(old_tail.key)
        return old_tail.key


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)