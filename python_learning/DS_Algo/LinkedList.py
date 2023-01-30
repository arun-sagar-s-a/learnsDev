# Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # get node value
    def get_vlaue(self):
        return self.value
    # get next node

    def get_next_node(self):
        return self.next_node
    # set next node, values shouldnt be set

    def set_next_node(self, next_node):
        self.next_node = next_node

# linked list class


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    # get head node
    def get_head_node(self):
        return self.head_node
    # add node at beginning

    def add_node_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
