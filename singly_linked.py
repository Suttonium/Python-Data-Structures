class Node:
    def __init__(self, value=None, next_node=None):
        """
        Simple Node class assigning a value and a pointer to the next node in the list
        By default, the value and next node are set to None to account for the Head and Tail
        :param value: value within Node
        :param next_node: pointer to the next Node in the list
        """
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        """
        SinglyLinkedList constructor creating the Tail, Head, and Current pointers
        """
        self.tail = Node()
        self.current = self.tail
        self.head = Node(next_node=self.tail)
        self.list_size = 0

    def insert(self, value):
        """
        insert a new Node at the current position in the list
        :param value: value within the Node to be inserted
        """
        self.current.next = Node(self.current.value, self.current.next)
        self.current.value = value
        if self.tail == self.current:
            self.tail = self.current.next
        self.list_size += 1

    def move_to_start(self):
        """
        Move the current Node to the start of the list
        """
        self.current = self.head.next

    def remove(self):
        """
        Remove the Node at the current position in the list
        """
        if self.current == self.tail:
            return
        self.current.value = self.current.next.value
        if self.current.next == self.tail:
            self.tail = self.current
        self.current.next = self.current.next.next

    def __str__(self):
        """
        String representation of the SinglyLinkedList
        :return: the string representation of the SinglyLinkedList
        """
        self.move_to_start()
        linked_list = "[H|-]"
        while self.current != self.tail:
            linked_list += '->[' + self.current.value + "|-]"
            self.current = self.current.next
        linked_list += '->[/|T]'
        return linked_list
