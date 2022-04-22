"""
A linear data structure where the elements are not stored in contiguous order in memory.

Two types : 
[1] Singly linked list
[2] Doubly linked list

Linked List 
    [장점]
        1. Array와는 다르게, 정렬이 되어있어도 특정 element 를 찾기 위해서는 O(n)의 시간복잡도가 필요하다.
    [단점]
        1. Insertion & Dletions 이 list에 비해 싸다. 
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    def insertNode(self, val, pos):
        target = Node(val)
        if pos == 0:
            target.next = self.head
            self.head = target
            return
        
        def getPrev(pos):
            temp = self.head
            count = 1
            while count < pos:
                temp = temp.next
                count += 1
            return temp

        prev = getPrev(pos)
        nextNode = prev
        prev.next = target
        target.next = nextNode

# Node Structure : 5 -> 1 -> 3 -> 7

linked_list = LinkedList()
linked_list.head = Node(5)
second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()