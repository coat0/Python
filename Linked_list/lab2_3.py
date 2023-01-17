#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Any
from lab2_1 import LinkedList


class Queue:
    _storage: LinkedList

    def __init__(self, _storage: LinkedList = LinkedList()) -> None:
        self._storage = _storage

    def __len__(self) -> int:
        return self._storage.len()

    def __str__(self) -> str:
        return self.print()

    def peek(self) -> int:
        first = self._storage.node(0)
        return first.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> int:
        poped = self._storage.pop()
        return poped.value

    def print(self) -> str:
        result = ''
        current = self._storage.head
        while current:
            result += str(current.value)
            if current.next:
                result += ', '
            current = current.next
        return result


queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

