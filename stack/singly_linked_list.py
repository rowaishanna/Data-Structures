class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __str__(self):
        return f'Linked List, Head: {self.head}, Tail: {self.tail}'



    def add_to_tail(self, value):
        # make a new node with the value and a next value of none
        new_node = Node(value, None)
        # check if there is no head
        if self.head is None:
            # set the head and the tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node






    def remove_head(self):
        # check if there is no head
        if self.head is None:
            return None
        # does our head have a next value?
        # if not, there is only one element in the list
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        # return value
        return value





    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None:
            return None
        # does our head have a next value?
        # if not, there is only one element in the list
        if self.head.get_next() is None:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        current.set_next(None)
        return value