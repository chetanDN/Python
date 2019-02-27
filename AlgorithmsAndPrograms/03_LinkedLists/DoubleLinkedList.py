class Node:

    #  constructor
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class DoubleLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_at_beg(self,node):
        #  new_node = Node(data, None, None)
        new_node = node
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = None
            new_node.next = self.head   # make the new node to point current DLL first node
            self.head.prev = new_node          # make the DLL first node's prev pointer to point new beginning node
            self.head = new_node

    def add_at_end(self,node):
        new_node = node
        if self.head == None:
            self.head = self.tail = new_node
        else:
            current_node = self.head            #loop through to last node, if you have tail pointer just use that
            while(current_node.next != None):
                current_node = current_node.next

            new_node.prev = current_node # make new node previous pointer to point last node
            current_node.next = new_node # erase None of last node next to new node

            self.tail = new_node
            '''
            new_node.prev = self.tail # make new node prev pointer to point current last node
            self.tail.next = new_node # make current last node pointer to point to new node

            self.tail = new_node # update tail pointer
            '''

    def print_list(self):
        # node_list = []
        print("print_list in DoubleLinkedList.py")
        current_node = self.head
        while current_node != None:
            # node_list.append(current_node.data)
            print(current_node.data,end=' ')
            current_node = current_node.next

DLL1 = DoubleLinkedList()
DLL1.add_at_beg(Node(1))
DLL1.add_at_beg(Node(2))
DLL1.add_at_end(Node(7))
DLL1.add_at_beg(Node(3))
DLL1.add_at_end(Node(9))

print('\n'+'*'*56)
DLL1.print_list()
