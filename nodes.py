# Joe Degere
# 2/24/2020
# Nodes homework; Advanced


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def add_head(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data=data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        curr_node = self.head
        prev_node = self.head
        while curr_node.next:
            prev_node = curr_node
        curr_node = curr_node.next
        prev_node.next = None
        return curr_node.data

    def clear_list(self):
        self.head = None

    def search(self, data):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.item == data:
                print("Item found")
                return True
            n = n.abs
        print("item not found")
        return False
