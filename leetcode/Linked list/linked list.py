#!/usr/bin/env python
# coding: utf-8

# In[198]:


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class MyLinkedList(object):

    def __init__(self, head = None):
        self.head = head
        
    def get(self, index):
        if self.head == None:
            return -1
        cur = 0
        cur_node = self.head
        nexxt_node = cur_node.next
        while cur_node != None:
            if index == cur :
                node = cur_node
                return node
            cur += 1 
            cur_node = nexxt_node
        return -1
        
    def addAtHead(self,data):
        if data is None:
            return None
        node = Node(data,self.head)
        self.head = node
        return node

    def addAtTail(self,data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node
    
    def addAtIndex(self, index, data):
        if index<0:
            node = Node(data,self.head)
            self.head = node
        cc = 1
        cur_node = self.head
        n_node = cur_node.next 
        while n_node != None:
            if index == cc:
                node = Node(data,n_node.next)
                n_node = node
                return node
            cc += 1 
            cur_node = n_node
        if index == cc+1:
            node = n_node(data)
            return node
        else:
            return None
    def deleteAtIndex(self, index) :
        if index<0:
            return None
        cc = 0
        cur_node = self.head
        n_node = cur_node.next 
        while cur_node != None:
            if index == cc:
                n_node = cur_node
            cc += 1 
            cur_node = n_node
        return None


# In[ ]:


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(1)
obj.addAtTail(5)
param_1 = obj.get(1)
obj.addAtIndex(1,6)
obj.deleteAtIndex(1)


# In[197]:


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# In[ ]:


def deleteAtIndex(self, index) :
    if index<0:
            return None
        cc = 0
        cur_node = self.head
        n_node = cur_node.next 
        while cur_node != None:
            if index == cc:
                n_node = cur_node
            cc += 1 
            cur_node = n_node
        return None

