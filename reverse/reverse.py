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

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # base case
        # if empty list return
        if node == None:
            return
        # get_next is self.next_node()
        innert_next = node.get_next()

        # if not at head, set next to prev node
        if not prev == None: 
            # 0 => 1 => 2 =>
            # 1 => 2 =>
            node.set_next(prev)
        # if not at the end keep going
        if not innert_next == None:
            # x at 2
            self.reverse_list(innert_next, node)
        # if it is the end, set tail to new head 
        else:
            self.head = node



        






