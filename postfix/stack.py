# stack.py
# Aidan Nachi
# 2024.31.3
# This file defines a Stack classes with the usual behaviors
# of a stack.
#
# The file defines a stack class that is constructed from a linked list. 
# The class includes the usual behaviors of a stack including push,
# pop, and checking to see if the stack is empty. The file additionally defines
# two more classes, a linked list node class that creates the nodes for the
# linked list our stack is built out of and a peek class that includes a funtion
# to check the top value of the stack. The peek class is kept seperate from the
# two stack classes in order to preserve the purity of the stack classes.
#
# Usage
# from stack import linked_list_stack, peek_stack


class Linked_list_stack():
    """ Implement a Stack object with a Linked List. """

    def __init__(self):
        """ Create a stack object. """

        # Points at the first values location in the list.
        self.head = None

    def push(self, value):
        """ Insert value at the top of the stack. """

        # Create a new node and place it at the top of the stack.
        new_node = Linked_list_stack_node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """ Remove and return value at the top of the stack. """

        # Grab and pull out top node from the stack.
        pop_node = self.head
        self.head = pop_node.next
        return(pop_node.data)

    def is_empty(self):
        """ Check if the stack is empty. """

        return(self.head == None)


class Linked_list_stack_node():
    """ Implement a node object for the linked list. """

    def __init__(self, value):
        """ Initialize a new instance of the Linked_list_stack class. """

        # Instance variables
        # data - holds the value in a node.
        # next - points to the next nodes location.
        self.data = value
        self.next = None


class Peek_stack(Linked_list_stack):
    """ Implement a Peek class. """

    def __init__(self):
        """ Initialize a new instance of the Peak class. """

        super().__init__()


    def peek_stack_value(self):
        """ Check value at top of the stack. """

        # Take out the value at the top of the stack and stick
        # it back in at the top of the stack.
        temp = self.pop()
        self.push(temp)
        return temp

