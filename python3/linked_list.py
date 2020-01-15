class LinkedList:
    def __init__(self, ll_name):
        self.ll_name = ll_name
        self.head = None
        self.length = 0

    def add_node(self, node_data, required_position=None):
        if required_position == None:
            if self.head is None:
                new_node = Node(node_data)
                self.head = new_node
                self.tail = new_node
                self.length += 1
                return True
            else:
                new_node = Node(node_data)
                self.tail.next_node = new_node
                self.tail = new_node
                self.length += 1
                return True
        else:
            if required_position > 1 and self.length == 0:
                print(" : ERROR : Linked List Length is : " + str(self.length))
                return False
            else:
                if required_position == 1:
                    new_node = Node(node_data)
                    new_node.next_node = self.head
                    self.head = new_node
                    self.length += 1
                    return True

                current_position = 0
                current_node = self.head
                while True:
                    current_position += 1
                    if current_position == required_position:
                        pass
                    else:
                        current_node = current_node.next_node

    def dump_ll(self):
        print("")
        print(" Linked List : " + self.ll_name)
        print("")
        print(" ", end="")
        start = self.head
        while True:
            print(str(start.node_data), end="")
            if start.next_node is None:
                break
            else:
                print(" > ", end="")
                start = start.next_node


class Node:
    def __init__(self, node_data=None, next_node=None):
        self.node_data = node_data
        self.next_node = next_node


ll_inst = LinkedList(input(" Enter the List Name : "))
ll_inst.add_node(1)
ll_inst.add_node(2)
ll_inst.add_node(3)
ll_inst.add_node(4)
ll_inst.add_node(5)
ll_inst.dump_ll()
print("")
