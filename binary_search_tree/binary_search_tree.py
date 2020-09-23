"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from stack import Stack
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False
    
    def __str__(self):
        return f'Value: {self.value}, Left: {self.left}, Right: {self.right}'

    # Insert the given value into the tree
    def insert(self, value):        
        # if value is greater than or equal to self.value
        if value >= self.value:
            # if self.right is None
            if self.right is None:
                # create a new node with the value
                # and set it equal to value
                node = BSTNode(value)
                self.right = node
            # otherwise repeat the equation recursively on the next node
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                # create a new node with the value
                # and set it equal to value
                node = BSTNode(value)
                self.left = node
            # otherwise repeat the equation recursively on the next node
            else:
                self.left.insert(value)
            
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value is target
        if self.value is target:
            return True
        # move right?
        if target > self.value:
            # is there a node to the right?
            if self.right is None:
                return False
            else:
                # otherwise repeat the equation recursively on the next node
                return self.right.contains(target)
        # move left
        if target < self.value:
            # is there a node to the left?
            if self.left is None:
                return False
            else:
                # otherwise repeat the equation recursively on the next node
                return self.left.contains(target)

        

    # Return the maximum value found in the tree
    def get_max(self):
        # is there one node?
        if self.right is None:
            # return the only value in the tree
            return self.value
        else:
            return self.right.get_max()
    
    # return the minimum value found in the tree
    def get_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # run the function on the current node
        fn(self.value)
        # Does the current node have a left?
        if self.left is not None:
            # repeat this method recursively
            self.left.for_each(fn)
        # Does the current node have a right?
        if self.right is not None:
            # repeat this metod recursively
            self.right.for_each(fn)
        return

    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # is there a node to the left?
        if self.left is not None:
            # recursively call this method on the left child node
            self.left.in_order_print()
        # if there is no node to the left, print the node's value
        print(self.value)
        # if there is a node to the right...
        if self.right is not None:
            # call this method recursively on that node
            self.right.in_order_print()
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a new queue
        new_q = Queue()
        # set current node
        current = self
        # add the current node to the queue
        new_q.enqueue(current)
        # make a while loop that will print things until the queue is empty
        while new_q.size > 0:
            # set current to the node that is being dequeued
            current = new_q.dequeue()
            # print its value
            print(current.value)
            # if the current node has a left node
            if current.left is not None:
                # add it to the queue
                new_q.enqueue(current.left)
            # if the current node has a right node
            if current.right is not None:
                # add it to the queue
                new_q.enqueue(current.right)
            
            



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a new stack
        new_stack = Stack()
        # push self to stack
        new_stack.push(self)
        # set current node to self
        current = self
        # print current node's value
        print(current.value)
        # while there are items in the stack...
        while new_stack.size > 0:
            # change the visited status to True
            current.visited = True
            # if the current node has a left child node that hasn't been visited
            if current.left is not None and current.left.visited is False:
                # add it to the stack
                new_stack.push(current.left)
                # change current to the left child node
                current = current.left
                # print the current node's value
                print(current.value)
            # if the current node has a right child node that hasn't been visited
            elif current.right is not None and current.right.visited is False:
                # add it to the stack
                new_stack.push(current.right)
                # change current to the left child node
                current = current.right
                # print the current node's value
                print(current.value)
            # otherwise...
            else:
                # set the current node to the node at the top of the stack
                # and pop it off
                current = new_stack.pop()
            
            

        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


# This code is necessary for testing the `print` methods

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

'''print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft() '''