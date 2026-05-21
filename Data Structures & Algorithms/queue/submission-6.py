class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.tail = Node(-1)
        self.head = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        lastNode = self.tail.prev

        lastNode.next, self.tail.prev = newNode, newNode
        newNode.next, newNode.prev = self.tail, lastNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        firstNode = self.head.next

        firstNode.prev, self.head.next = newNode, newNode
        newNode.prev, newNode.next = self.head, firstNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        newTail = self.tail.prev
        val = newTail.val
        prevNode = newTail.prev

        prevNode.next = self.tail
        self.tail.prev = prevNode
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        newHead = self.head.next
        val = newHead.val
        nextNode = newHead.next
        nextNode.prev = self.head
        self.head.next = nextNode
        return val
        
        return val
