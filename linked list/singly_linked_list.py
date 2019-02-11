
# coding: utf-8

# In[2]:


#create nodes
#create linkded list
#add nodes to linked list
#print linked list


# In[186]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# In[187]:


class LinkedList:
    def __init__(self):
        self.head = None
    
    def list_length(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count 
    
    def is_list_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node
    
    def insert_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
            del temp_node
    
    def insert_at(self, new_node, position):
        current_position = 0
        if position is 0:
            self.insert_head(new_node)
            return
        if position < 0 or position >= self.list_length():
            print("Element cannot be inserted at given position")
            return
        if self.head is None:
            print("Linked list is empty")
        else:
            cur_node = self.head
            while True:
                if current_position == position:
                    prev_node.next = new_node
                    new_node.next = cur_node
                    break
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    current_position += 1
        
        
    def print_list(self):
        if self.head is None:
            print("Linked list Elements are none")
        else:
            cur_node = self.head
            while True:
                if cur_node is not None:
                    print(cur_node.data)
                    cur_node = cur_node.next
                else:
                    break
                    
    def del_end(self):
        cur_node = self.head
        if self.is_list_empty():
            print('List is empty')
        else:
            while cur_node.next is not None:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = None
    
    def del_head(self):
        if self.is_list_empty():
            print("list is empty")
        else:
            if self.head.next is None:
                self.del_end()
                return
            prev_head = self.head
            self.head = self.head.next
            prev_head.next = None
    
    def del_position(self, position):
        cur_position = 0
        cur_node = self.head
        if position is 0:
            self.del_head()
            return
        if position < 0 or position >= self.list_length():
            print('This position is not exist')
            return
        if self.is_list_empty():
            print('List is empty')
        while True:
            if cur_position == position:
                prev_node.next = cur_node.next
                cur_node.next = None
                break
            else:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_position += 1


