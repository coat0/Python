#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any = None, left_child: 'BinaryNode' = None, right_child: 'BinaryNode' = None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def min(self) -> 'BinaryNode':
        current: BinaryNode = self
        while current.left_child:
            current = current.left_child
        return current

    def contains(self, value: Any) -> bool:
        if value == self.value:
            return True

        if value < self.value:
            if self.left_child is None:
                return False
            return self.left_child.contains(value)

        if self.right_child is None:
            return False
        return self.right_child.contains(value)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self):
        self.root = BinaryNode()

    def insert(self, value: Any) -> None:
        if not self.root.value:
            self.root.value = value
        else:
            self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, val: Any):
        if val < node.value:
            if node.left_child:
                node.left_child = self.__insert(node.left_child, val)
                return node
            node.left_child = BinaryNode(val)
        if val >= node.value:
            if node.right_child:
                node.right_child = self.__insert(node.right_child, val)
                return node
            node.right_child = BinaryNode(val)
        return node

    def insertlist(self, list) -> None:
        for x in list:
            self.insert(x)

    def contains(self, value) -> bool:
        return self.root.contains(value)

    def remove(self, value: Any) -> None:
        self.root = self.__remove(self.root, value)

    def __remove(self, node: BinaryNode, value: Any):
        if node is not None:
            if node.value == value:
                if node.left_child is None and node.right_child is None:
                    return None
                if node.left_child is None:
                    return node.right_child
                if node.right_child is None:
                    return node.left_child
                node.value = node.right_child.min().value
                node.right_child = self.__remove(node.right_child, node.value)
            if value < node.value:
                node.left_child = self.__remove(node.left_child, value)
            if value > node.value:
                node.right_child = self.__remove(node.right_child, value)
            return node

    def show(self) -> None:
        if self.root:
            if self.root.right_child:
                if self.root.right_child.right_child:
                    if self.root.right_child.right_child.right_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.right_child.right_child.right_child.value)
                        print()
        if self.root:
            if self.root.right_child:
                if self.root.right_child.right_child:
                    for x in range(20):
                        print(' ', end='')
                    print(self.root.right_child.right_child.value)
                    print('')
        if self.root:
            if self.root.right_child:
                if self.root.right_child.right_child:
                    if self.root.right_child.right_child.left_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.right_child.right_child.left_child.value)
                        print()
        if self.root:
            if self.root.right_child:
                for x in range(10):
                    print(' ', end='')
                print(self.root.right_child.value)
                print('')
        if self.root:
            if self.root.right_child:
                if self.root.right_child.left_child:
                    if self.root.right_child.left_child.right_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.right_child.left_child.right_child.value)
                        print()
        if self.root:
            if self.root.right_child:
                if self.root.right_child.left_child:
                    for x in range(20):
                        print(' ', end='')
                    print(self.root.right_child.left_child.value)
                    print('')
        if self.root:
            if self.root.right_child:
                if self.root.right_child.left_child:
                    if self.root.right_child.left_child.left_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.right_child.left_child.left_child.value)
                        print()
        if self.root:
            print(self.root.value)
            print('')
        if self.root:
            if self.root.left_child:
                if self.root.left_child.right_child:
                    if self.root.left_child.right_child.right_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.left_child.right_child.right_child.value)
                        print('')
        if self.root:
            if self.root.left_child:
                if self.root.left_child.right_child:
                    for x in range(20):
                        print(' ', end='')
                    print(self.root.left_child.right_child.value)
                    print('')
        if self.root:
            if self.root.left_child:
                if self.root.left_child.right_child:
                    if self.root.left_child.right_child.left_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.left_child.right_child.left_child.value)
                        print('')
        if self.root:
            if self.root.left_child:
                for x in range(10):
                    print(' ', end='')
                print(self.root.left_child.value)
                print('')
        if self.root:
            if self.root.left_child:
                if self.root.left_child.left_child:
                    if self.root.left_child.left_child.right_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.left_child.left_child.right_child.value)
                        print('')
        if self.root:
            if self.root.left_child:
                if self.root.left_child.left_child:
                    for x in range(20):
                        print(' ', end='')
                    print(self.root.left_child.left_child.value)
        if self.root:
            if self.root.left_child:
                if self.root.left_child.left_child:
                    if self.root.left_child.left_child.left_child:
                        for x in range(30):
                            print(' ', end='')
                        print(self.root.left_child.left_child.left_child.value)


tree1 = BinarySearchTree()
listunia = [8, 3, 1, 6, 4, 7, 10, 14, 13, 15]
# listunia = [6, 7, 4]
tree1.insertlist(listunia)

print(tree1.contains(13))
tree1.show()

