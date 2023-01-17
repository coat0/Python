#!/usr/bin/env python
# coding: utf-8
# In[ ]:


from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any = None, next: 'Node' = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head: Node = None, tail: Node = None) -> None:
        self.head = head
        self.tail = tail

    def __str__(self):
        return self.print()

    def push(self, value: Any) -> None:
        newNode = Node(value)
        if self.head:
            temp = self.head
            self.head = newNode
            current = self.head
            current.next = temp
        else:
            self.head = newNode
            if self.tail == None:
                self.tail = newNode

    def append(self, value: Any) -> None:
        newNode = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def node(self, at: int) -> Node:
        i: int = 0
        current = self.head
        while i < at:
            current = current.next
            i += 1
        return current

    def insert(self, value: Any, after: Node) -> None:
        newNode = Node(value)
        temp = after.next
        after.next = newNode
        newNode.next = temp

    def print(self) -> str:
        current = self.head
        result = ''
        while current:
            result += str(current.value)
            if current.next:
                result += ' -> '
            current = current.next
        return result

    def pop(self) -> Node:
        poped = self.head
        self.head = poped.next
        return poped

    def remove_last(self) -> Node:
        current = self.head
        newlast = self.tail
        while current.next:
            newlast = current
            current = current.next
        newlast.next = None
        self.tail = newlast
        return current

    def remove(self, after: Node) -> None:
        after_after = after.next
        after.next = after_after.next

    def len(self) -> int:
        i: int = 0
        current = self.head
        while current:
            current = current.next
            i += 1
        return i


# list_ = LinkedList()
#
# list_.push(1)
# list_.push(0)
#
# print(list_)

