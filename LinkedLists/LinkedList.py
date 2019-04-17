from LinkedLists.Node import Node


class LinkedList:
    tail = None
    head = None
    count = 0

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None

    # Function to insert a new node at the beginning
    def insertatbegining(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = self.head
        self.count += 1

    # Function to insert a new node at the end
    def insertatend(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = self.tail = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
        self.count += 1

    # Function to display all the elements of List
    @staticmethod
    def display(head):
        temp = head
        while temp is not None:
            print(" ", temp.data, " ")
            temp = temp.nextNode

    # Function to display data in the last Element
    def tailelement(self):
        if self.tail is None:
            return None
        return self.tail.data

    # Function to display data in the First Element
    def headelement(self):
        if self.head is None:
            return None
        return self.head.data

    # Function to delete element from linked list
    def delete(self, data):
        if self.head == self.tail and self.head is None:
            return None
        temp = self.head
        # If linked list contains only one element
        if self.head == self.tail:
            temp.data = None
            temp.nextNode = None
            self.count -= 1
            self.head = self.tail = None
            return
        if self.head.data == data:
            self.head = self.head.nextNode
            del temp
            return
        prev = temp
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.nextNode
        # if data was not present in linked list
        if temp is None:
            return
        # if data is at the end of list
        if temp.nextNode is None:
            self.tail = prev
        # Unlink the node from linked list
        prev.nextNode = temp.nextNode
        temp.data = None
        temp.nextNode = None
