# Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # get node value
    def get_value(self):
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

    # display Linked List
    def display(self):
        temp_node = self.get_head_node()  # node
        # print(temp_node.get_value())
        while (temp_node != None):
            print(temp_node.get_value())
            temp_node = temp_node.get_next_node()

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        temp_node = current_node.get_next_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            print(f"Removed : {value_to_remove}")
            self.display()
        else:
            while temp_node != None:
                if (temp_node.get_value() != value_to_remove):
                    current_node = current_node.get_next_node()
                    temp_node = temp_node.get_next_node()
                    continue
                else:
                    current_node.set_next_node(temp_node.get_next_node())
                    temp_node.set_next_node(None)
                    print(f"Removed : {value_to_remove}")
                    break
            else:
                print(f"{value_to_remove} is not present in linked list")
            self.display()


linked_list = LinkedList(10)
linked_list.add_node_beginning(12)
linked_list.add_node_beginning(13)
print("Display function")
linked_list.display()

print("Remove function")
linked_list.remove_node(12)
