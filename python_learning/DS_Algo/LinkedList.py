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

    # remove any node in Linked list
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

    # swap two nodes in Linked list
    def swap_nodes(self, val1, val2):
        # initialise defaults
        node1 = self.get_head_node()
        node2 = self.get_head_node()
        node1_prev = None
        node2_prev = None
        # if node1 and node2 are same no swap needed.
        if val1 == val2:
            print("No swapping necessary.")
            return
        # find val1 node
        while node1 is not None:
            if node1.get_value() == val1:
                break
            else:
                node1_prev = node1
                node1 = node1.get_next_node()
        else:
            print(f"{val1} is not present in LL so can't swap.")
            return
        # find val2 node
        while node2 is not None:
            if node2.get_value() == val2:
                break
            else:
                node2_prev = node2
                node2 = node2.get_next_node()
        else:
            print(f"{val2} is not present in LL so can't swap.")
            return

        # if prev node is non then current is head
        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
        # if prev node is non then current is head
        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        # finally swap the values
        temp_node = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp_node)


linked_list = LinkedList(10)
for i in range(9):
    linked_list.add_node_beginning(i)


print("Display function")
# linked_list.display()
# print("After swapp")
# print("Remove function")
# linked_list.remove_node(12)
linked_list.swap_nodes(1, 9)
print("Display function")
linked_list.display()
