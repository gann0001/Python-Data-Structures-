
# coding: utf-8

# In[122]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


# In[132]:


node_one = Node('Joe')
node_two = Node('Mary')
node_three = Node('Grace')


# In[277]:


class LinkedList:
    def __init__(self):
        self.head = None
    
    def list_len(self):
        count = 0
        cur_node = self.head
        if self.head is None:
            print('list is empty')
            return
        while True:
            if cur_node is None:
                return count
            else:
                count += 1
                cur_node = cur_node.next
                
    def insert_end(self,new_node):
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while True:
            if cur_node.next is None:
                break
            else:
                cur_node = cur_node.next
        cur_node.next = new_node
        new_node.previous = cur_node        
    
    def insert_head(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        new_node.next = temp
        temp.previous = new_node
        
    def insert_at(self, new_node, pos):
        cur_pos = 0
        if pos == linked_list.list_len():
            self.insert_end(new_node)
            return
        if self.head is None:
            print('List is empty')
            return
        if pos < 0 or pos > linked_list.list_len():
            print('cannot be insterted at given position')
            return
        if pos is 0:
            self.insert_head(new_node)
            return
        cur_node = self.head
        while True:
            if cur_pos == pos:
                cur_node.previous.next = new_node
                new_node.previous = cur_node.previous
                new_node.next = cur_node
                cur_node.previous = new_node
                break
            else:
                cur_node = cur_node.next
                cur_pos += 1
        
    def del_end(self):
        cur_node = self.head
        while True:
            if cur_node.next.next is None:
                temp = cur_node.next
                cur_node.next = None
                temp.previous = None
                break
            else:
                cur_node = cur_node.next
    
    def del_head(self):
        self.head = self.head.next
        self.head.previous.next = None
        self.head.previous = None
    
    def del_inbetween(self, data):
        if self.head.data == data:
            del_head()
            return
        cur_node = self.head
        while True:
            if cur_node.data == data:
                cur_node.previous.next = cur_node.next
                cur_node.next.previous = cur_node.previous
                cur_node.next = None
                cur_node.previous = None
                break
            else:
                cur_node = cur_node.next
        
    def print_list(self):
        cur_node = self.head
        if cur_node is None:
            print('List is empty')
            return
        print('printing from the begining:')
        while True:
            if cur_node is None:
                break
            print(cur_node.data)
            if cur_node.next is None:
                last_node = cur_node
            cur_node = cur_node.next
        
        print('\nprinting from the backward:')
        while True:
            if last_node is None:
                break
            print(last_node.data)
            last_node = last_node.previous
    