

class Node:

    #constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None

    #setter method for data
    def set_data(self, data):
        self.data = data

    #getter method for data
    def get_data(self):
        return self.data

    #method for setting the next field
    def set_next(self, next):
        self.next = next

    #method for getting the next field
    def get_next(self):
        return self.next

    #check next node exists
    def has_next(self):
        return self.next != None

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add_node(self, node):
        if self.length == 0:
            self.add_at_beg(node)
        else:
            self.add_at_end(node)

    def add_at_beg(self,node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def add_at_end(self,node):

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        new_node = node
        new_node.next = None
        current_node.next = new_node

        self.length += 1

    def add_at_pos(self, pos, node):

        if pos >= (self.length + 1) or pos < 0: #is total length is 4 , new pos could be 0 to 3 and 4 to add new element, if pos is > 4 i.e 5 onwards  print fail condition, and pos cannot be -ve
            print("enter valid position, length of ll is ",self.length)
        else:
            print('entered position is valid')
            if pos == 0: #even is one ele in ll, it has pos 0 and 1 to add new ele at pos beginning(0) and add at end(1)
                self.add_at_beg(node)
            elif pos == self.length:
                self.add_at_end(node)
            else:
                print('have to add in middle')
                current_node = self.head
                print("type of current_node",type(current_node.))
                print("type of node passed",type(node))
                previous_node = self.head
                count = 0 #increment current pointer till previous node to inserting node
                while count < pos-1 : #traverse to get one node previous's info in current_node
                    current_node = current_node.next  #current_node.get_next() will not work , type mis match
                    count = count + 1

                node.next = current_node.next #node.set_next(current_node.next) - woeks
                current_node.next = node

                self.length += 1

    def print_list(self):
        # node_list = []

        current_node = self.head
        while current_node != None:
            # node_list.append(current_node.data)
            print(current_node.data)
            current_node = current_node.next

        # print(node_list)


node1 = Node(1)
node2 = Node(2)
node3 = Node()
node3.set_data(3)
node4 = Node(4)

ll1 = LinkedList()
ll1.add_node(node1)
ll1.add_node(node2)
# ll1.add_node(node3)
ll1.add_at_pos(1, node4)

ll1.print_list()