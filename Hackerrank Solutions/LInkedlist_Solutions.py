
#QQ# Print the Elements of a Linked List
"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def print_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

#QQ# Insert a Node at the Tail of a Linked List

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    print (head.__class__)
    if head == None:
        node.next = None
        head = node
    else:
        curr = head
        while curr != None:
            t = curr
            curr = curr.next
        t.next = node
        node.next = None

    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()


#QQ# Insert a node at the head of a linked list


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # print (SinglyLinkedListNode())
    # Write your code here
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node


#QQ# Insert a node at a specific position in a linked list

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    temp = None
    curr = head
    while position != 0:
        temp = curr
        position = position -1
        curr = curr.next
    temp.next = node
    node.next = curr
    return head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()


#QQ# Delete a Node


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    temp = head
    temp_after = head.next.next

    curr = head
    if position == 0:
        return head.next
    while position != 0:
        # print (curr.data)
        temp = curr

        curr = curr.next
        position = position - 1
        if curr != None:
            temp_after = curr.next
    temp.next = temp_after

    return head

#QQ# Print in Reverse

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def ReversePrint(head):
    lst = []
    curr = head
    while curr:
        # print( curr.data,'s')
        lst.append(curr.data)
        curr = curr.next
    # lst.append(curr.data)
    lst = lst[::-1]
    # print (lst)
    for val in lst:
        print(val)


#QQ# Reverse a linked list

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    prev = None
    curr = head
    fut = head
    while fut:
        curr = fut
        fut = fut.next
        curr.next = prev
        prev = curr

    head = curr
    return curr


#QQ# Get Node Value

# Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    ret = count - position

    curr = head
    count = 0
    while curr:
        count += 1
        if count == ret:
            return curr.data
        curr = curr.next



#QQ# Delete duplicate-value nodes from a sorted linked list

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    curr = head
    prev = head
    while curr:
        lst = []
        prev = curr
        curr = curr.next
        while curr != None and prev.data == curr.data:
            prev.next = curr.next
            curr = curr.next

    return head




