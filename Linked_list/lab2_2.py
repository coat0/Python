#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Any
from lab2_1 import LinkedList


class Stack:
    _storage: LinkedList

    def __init__(self, _storage: LinkedList = LinkedList()) -> None:
        self._storage = _storage

    def __len__(self) -> int:
        return self._storage.len()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> int:
        poped = self._storage.pop()
        return poped.value

    def print(self) -> None:
        current = self._storage.head
        while current:
            print(current.value)
            current = current.next


stack = Stack()
stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

stack.print()





