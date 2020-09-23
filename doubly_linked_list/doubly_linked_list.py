"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # add a node to the head
        # make sure its next node is the current head
        new_node = ListNode(value, next=self.head)

        # If this is an empty list...
        if self.head is None:
            # set head equal to new node
            self.head = new_node
            # set tail equal to new node
            self.tail = new_node
            # change the size
            self.length += 1

        # if there are already nodes in the list...
        else:
            # set the current head's previous node to the new node
            self.head.prev = new_node
            # set the new node as the head of the list
            self.head = new_node
            # change the size
            self.length += 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Is this an empty list?
        if self.head is None:
            return None

        # Is there only one element in the list?
        if self.head.next is None:
            # Store the current value of head
            head = self.head.value
            # set the head and tail to none
            self.head = None
            self.tail = None
            # change length
            self.length -= 1
            # return the value
            return head

        # Store the current head's value    
        head = self.head.value
        # reassign head to the next node
        self.head = self.head.next
        # set the head's prev node to none
        self.head.prev = None
        # change length
        self.length -= 1
        return head
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new node to add to the list
        # set the previous node as the current list's tail
        new_node = ListNode(value, prev=self.tail)
        # what if it's an empty list?
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            tail = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return tail
        
        # store the value of the tail
        tail = self.tail.value
        # set the tail to the current tail's previous node
        self.tail = self.tail.prev
        # set the new tail's next node to none
        self.tail.next = None
        # change the length
        self.length -= 1
        # return the value of the previous tail
        return tail


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if it is an empty list, set the node to head and tail
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return
        # if there is only one node, do nothing
        if self.length is 1:
            return
        # if the node is already at the head
        if self.head is node:
            return
        # if the node is the tail of the list
        if self.tail is node:
            # Change the tail to second to last node
            self.tail = node.prev
            # break the chain
            self.tail.next = None
            node.prev = None
            # set head's prev node to node
            self.head.prev = node
            # set node's next node to the current head
            node.next = self.head
            # set the node as the head
            self.head = node
            return
        # otherwise...
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if it's an empty list
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        # if it has only one element
        if self.length is 1:
            return

        # if it's already the tail
        if self.tail is node:
            return 

        # if the node is the head
        if self.head is node:
            self.head = node.next
            self.head.prev = None
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return
        
        # otherwise...
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node 

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if it is an empty list
        if self.head is None:
            return
        # if it contains a single node
        if self.length is 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        # if the node is the head
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            self.length -= 1
            return
        # if the node is the tail
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
            self.length -= 1
            return
        # otherwise...
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length is 0:
            return
        
        counter = self.head
        max_val = counter.value
        
        while counter.next is not None:
            counter = counter.next
            if counter.value > max_val:
                max_val = counter.value

        return max_val    