"""

A linked list where a node have pointers to both previous and next node.


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def creatList(self, arr):

        start = self.head
        n = len(arr)
        i = 0

        while i<n:
            newNode = Node(arr[i])
            if (i == 0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)

    def countList(self):
        temp = self.head
        count = 0 

        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def insertAtLocation(self, value, index):
        temp = self.head

        count = self.countList()

        if count+1 < index:
            return temp
        
        newNode = Node(value)

        if index == 1:
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head
        
        if index == count + 1:
            while temp.next is not None:
                temp = temp.next
            
            temp.next = newNode
            newNode.prev = temp
            return self.head

        i = 1
        while i < index-1:
            temp = temp.next
            i += 1
        
        nodeAtTarget = temp.next
        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode
        temp.next = newNode
        newNode.prev = temp

        return self.head

    def deleteAtLocation(self, index):
        temp = self.head

        count = self.countList()

        if count < index:
            return temp

        if index == 1:
            temp = temp.nexst
            self.head = temp
            return self.head

        i = 1
        if index == count:
            while i < index-1:
                temp = temp.next
                i += 1
            
            targetNode = temp.next
            targetNode = None
            temp.next = None

        i = 1
        if 1 < index and index < count:
            while i != index-1:
                temp = temp.next
                i += 1
            targetNode = temp.next
            temp.next = targetNode.next
            targetNode.next.prev = temp

            targetNode = None
            


        


# 1 -> 2 -> 3 -> 4 -> 5
arr = [1,2,3,4,5]

llist = LinkedList()
llist.creatList(arr)
llist.insertAtLocation(77,3)
llist.printList()
