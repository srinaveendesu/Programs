class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    

##node1 = Node(11)
##node2 = Node(12)
##node3 = Node(13)
##print (node1,node2,node3)
##
##node1.next_node = node2
##node2.next_node = node3
##
##
##print(node1, node1.next_node)

class Sll(object):
    
    def __init__(self, head= None):
        self.head = head
        self.tail = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.set_next(new_node)
        self.tail = new_node

    def insert_head(self, data):
        new_node = Node(data,self.head)
        self.head = new_node
        

    def insert_between(self, data , index_value):
        #will work only after it has min of one node
        count = 0
        siz = self.size()
        prev = self.head
        curr = self.head
        while curr:
            count +=1
            #inserting between head and first node
            if index_value ==1 and count == index_value :
                new_node = Node(data,curr)
                self.head = new_node
                return
            #inserting between two nodes
            elif count == index_value:
                new_node = Node(data,curr)
                prev.next_node = new_node 
                return
            prev = curr
            curr = curr.get_next()

    def linked_reverse1(self):
        prev = self.head
        curr = self.head
        temp = None
        while curr:
            prev = curr
            curr = curr.get_next()
            if prev == self.head:
                prev.next_node = None
                temp = prev
            elif prev.next_node != None:
                prev.next_node = temp
                temp = prev
            elif not prev.next_node:
                prev.next_node = temp
                self.head = prev
                
    def linked_reverse2(self):
        prev = None
        curr = None
        nexx = self.head
        while nexx:
            curr = nexx
            nexx = curr.next_node
            curr.next_node = prev
            prev = curr
        self.head = curr

    def linkedlist_builder(self, head = None):
        lst = []
        curr = self.head
        if head:
            curr = head
        while curr:
            lst.append(str(curr.data))
            curr = curr.get_next()
        lst.append('None')
        return lst

    def delete(self,value):
        prev = self.head
        curr = self.head
        while curr:
            #deleting headnode
            if value == self.head.data:
                self.head = self.head.get_next()
                return
            #deleting rest of nodes
            elif value == curr.data:
                prev.next_node = curr.get_next()
                return
            prev = curr
            curr = curr.get_next()

    def increment(self):
        """incrementing linked list using indexing without reversing linked list method"""
        curr = self.head
        left = -1
        right = -1
        count_nine = 0
        count = 0
        #To find index of digits to be changed from left to right
        while curr:
            count = count +1
            if curr.data <9 :
                left = count
            elif curr.data ==9 :
                right = count
                count_nine +=1
            curr = curr.next_node
        count = 0
        curr = self.head
        #To increment the values as required
        while curr:
            count +=1
            if  left == count and curr.data <9:
                curr.data +=1
            elif left < count and count <= right and curr.data ==9:
                curr.data =0
            curr = curr.next_node
        if count == count_nine:
            new_node = Node(1)
            new_node.next_node = self.head
            self.head = new_node
            return

    def increment1(self):
        """incrementing linked list by 1 using reverse linked list method"""
        self.linked_reverse2()
        curr = self.head
        count_ele = 0
        count_nine =0
        while curr:
            count_ele = count_ele +1
            if curr.data<9:
                curr.data = curr.data+1
                break
            elif curr.data ==9:
                curr.data = 0
                count_nine +=1
            curr = curr.next_node
        self.linked_reverse2()        
        if count_ele == count_nine:
            new_node = Node(1)
            new_node.next_node = self.head
            self.head = new_node
            return

    def increment2(self):
        # To store the last node in the
        # linked list which is not equal to 9
        last = None
        cur = self.head

        # Iterate till the last node
        while (cur.next_node != None):
            if (cur.data != 9):
                last = cur
            cur = cur.next_node

        # If last node is not equal to 9
        # add 1 to it and return the head
        if (cur.data != 9):
            cur.data += 1
            return self.head

            # If list is of the type 9 -> 9 -> 9 ...
        if (last == None):
            last = Node()
            last.data = 0
            last.next_node = self.head
            self.head = last

            # For cases when the rightmost node which
        # is not equal to 9 is not the last
        # node in the linked list
        last.data += 1
        last = last.next_node

        while (last != None):
            last.data = 0
            last = last.next_node

        return self.head

    # Floyd’s Cycle-Finding Algorithm
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)
    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next_node):
            slow_p = slow_p.next_node
            fast_p = fast_p.next_node.next_node
            if slow_p == fast_p:
                return ("Found Loop")

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while (slow_p and fast_p and fast_p.next_node):
            slow_p = slow_p.next_node
            fast_p = fast_p.next_node.next_node

            # If slow_p and fast_p meet at some poin
            # then there is a loop
            if slow_p == fast_p:
                self.removeLoop(slow_p)

                # Return 1 to indicate that loop if found
                return "found"

                # Return 0 to indicate that there is no loop
        return "Not found"

    # Function to remove loop
    # loop_node --> pointer to one of the loop nodes
    # head --> Pointer to the start node of the linked list
    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node

        # Count the number of nodes in loop
        k = 1
        while (ptr1.next_node != ptr2):
            ptr1 = ptr1.next_node
            k += 1

        # Fix one pointer to head
        ptr1 = self.head

        # And the other pointer to k nodes after head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next_node

        # Move both pointers at the same place
        # they will meet at loop starting node
        while (ptr2 != ptr1):
            ptr1 = ptr1.next_node
            ptr2 = ptr2.next_node

        # Get pointer to the last node
        while (ptr2.next_node != ptr1):
            ptr2 = ptr2.next_node

        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next_node = None

    def firstSecondlargest(self):

        val1 = self.head.data
        val2 = self.head.next_node.data
        if val1 >val2:
            max1 = val1
            secondmax = val2
        else:
            max1 = val2
            secondmax = val1

        # move the head pointer to 3rd node
        curr = self.head.next_node.next_node.next_node

        while curr:
            if curr.data >max1:
                secondmax = max1
                max1 = curr.data
            elif curr.data > secondmax:
                secondmax = curr.data

            curr = curr.next_node
        return max1,secondmax

    def reversepalin(self, head):
        prev = None
        curr = None
        while head:
            curr = head
            head = curr.next_node
            curr.next_node = prev
            prev = curr
        return curr


    def isPalindrome(self):
        # get middle pointer
        p1 = self.head
        p2 = self.head
        while p2 and p2.next_node:
            p1 = p1.next_node
            p2 = p2.next_node.next_node

        secondpart = self.reversepalin(p1)

        # check palindrome
        p1 = secondpart
        p2 = self.head
        while p1:
            if p1.data == p2.data:
                p1 = p1.next_node
                p2 = p2.next_node
            else:
                return False

        self.reversepalin(secondpart)
        if secondpart:
            return True
        else:
            return False

    def swapPairs(self):
        curr = Node(0,self.head)
        self.head = curr
        while curr.next_node and curr.next_node.next_node:
            first = curr.next_node
            second = first.next_node
            curr.next_node, second.next_node, first.next_node = second, first, second.next_node
            curr = first
        self.head = self.head.next_node
        return self.head

    def swapPairs2(self):
        if not self.head or not self.head.next_node: return self.head
        cur = Node(0,self.head)
        self.head = cur

        while cur.next_node and cur.next_node.next_node:
            first = cur.next_node
            sec = cur.next_node.next_node
            cur.next_node = sec
            first.next_node = sec.next_node
            sec.next_node = first
            cur = cur.next_node.next_node
        self.head = self.head.next_node
        return self.head

    def reverseKGroup(self, k):
        start = Node(0,self.head)
        self.head = start
        l = r = start.next_node

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next_node
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                fast, cur = r, l

                for _ in range(k):
                    # standard reversing
                    nexx = cur.next_node
                    cur.next_node = fast
                    fast = cur
                    cur = nexx

                # connect two k-groups
                start.next_node = fast
                start = l
                l = r

            else:
                self.head = self.head.next_node
                return

    def removeNthFromEnd(self, n):
        curr = Node(0,self.head)
        self.head = curr
        fast = slow = self.head.next_node

        for _ in range(n):
            fast = fast.next_node

        while fast.next_node:
            fast = fast.next_node
            slow = slow.next_node

        slow.next_node = slow.next_node.next_node
        self.head = self.head.next_node
        return self.head


    def search(self, value):
        curr = self.head
        while curr:
            if value == curr.data:
                return ('Value found')
            curr = curr.get_next()
        return ('Value not found')

    def search_index(self, value):
        curr = self.head
        count = 0
        while curr:
            count = count +1
            if value == curr.data:
                return ('Value found at index',count )
            curr = curr.get_next()
        return ('Value not found')

    def size(self, head = None):
        return len(self.linkedlist_builder(head)) -1

    def __repr__(self,head= None):
        return '->'.join(self.linkedlist_builder(head))

def add(fnode, snode, mode =0):
    """Function to add two linked lists. the resultant linked list will be added
       to first linked list or to the bigger linked list
    """
    if mode==0:
        fnode.linked_reverse2()
        snode.linked_reverse2()
    f_len = fnode.size()
    s_len = snode.size()
    
    carry = 0
    #Smaller digit is added to bigger digit
    if s_len >f_len:
        temp = fnode
        fnode = snode
        snode = temp
    
    s_curr = snode.head
    f_curr = fnode.head
    
    #loop through smaller digit and keep adding
    while s_curr:
        #check if any carry from previous addition exists
        if carry ==0:
            data = s_curr.data + f_curr.data
        elif carry ==1:
            data = s_curr.data + f_curr.data + 1
            carry=0
        #After addition if total sum is more than 10 update carry flag
        #and change current value to mod of sum
        if data <10:
            f_curr.data = data
        elif data >=10 :
            data = data % 10
            f_curr.data = data
            carry = 1
        s_curr = s_curr.next_node
        f_curr = f_curr.next_node

    #if carry is 1 from previous calculation update the values
    #of bigger digit rest of values
    if carry == 1 and f_curr != None:#case when carry=1 and unequal digits are added
        if f_curr.data != 9:# when digit is not 9 simply add value
            f_curr.data = f_curr.data +1
        else:
            f_curr.data = 0
            while f_curr: # when digit is 9 simply pass the carry to other digits
                if f_curr.data ==9:
                    f_curr.data = 0
                f_curr = f_curr.next_node
            
            fnode.linked_reverse2()
            snode.linked_reverse2()
            fnode.insert_head(1)
            
            return fnode
        
    elif carry == 1 and f_curr == None:#case when carry=1 and equal digits are added
        fnode.linked_reverse2()
        snode.linked_reverse2()
        fnode.insert_head(1)    
        return fnode
    
    fnode.linked_reverse2()
    snode.linked_reverse2()
    return fnode


def addTwoNumbers( l1: Node, l2: Node) -> Node:
    l1.linked_reverse2()
    l2.linked_reverse2()

    l1 = l1.head
    l2 = l2.head
    s = Sll()
    c = 0
    while c != 0 or l1 != None or l2 != None:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        tot = val1 + val2 + c
        c = tot // 10

        s.insert(tot % 10)

        l1 = l1.next_node if l1 else l1
        l2 = l2.next_node if l2 else l2

    s.linked_reverse2()
    return s

def mergeTwoListsrecursive( a, b) :
    if a and b:
        if a.data > b.data:
            a, b = b, a
        a.next_node = mergeTwoListsrecursive(a.next_node, b)
    return a or b

def mergeTwoLists(l1, l2 ):
    l1 = l1.head
    l2 = l2.head
    s =Sll()
    s.insert(0)
    cur = s.head
    while l1 and l2:
        if l1.data < l2.data:
            cur.next_node = l1
            l1 = l1.next_node
        else:
            cur.next_node = l2
            l2 = l2.next_node
        cur = cur.next_node
    cur.next_node = l1 or l2
    s.head = s.head.next_node
    return s

def mergeKLists(lists):
    """
    time complexity o(nlogk)
    space complexity o(1)
    """
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists


s = Sll()
#print (s, s.head)
s.insert(11)

#print (s,s.head,s.head.next_node,'11',s.head.data)
s.insert(12)
s.insert_between(21,2)
print (s)
#print (s.head,s.head.data,s.head.next_node,s.head.next_node.data, s.head.next_node.next_node, )

#print (s.head, s.head.next_node,s.head.next_node.next_node,s)
s.insert(13)
#print (s.head, s.head.next_node,s.head.next_node.next_node,s)
s.insert(14)
s.insert(15)
#linked list and its size
print (s, s.size())
#linked list size when a head node is passed
print (s.size(s.head.next_node))
#linked list search
print (s.search(16), s.search(14))
#linked list func to get  index
print (s.search_index(14),s.search_index(20))

s.delete(14)
print (s, s.size())


s.insert_head(10)
print (s)

s.insert_between(14,5)
print (s)


s.insert_between(9,1)
print (s,s.head.data)

s.insert_between(16,8)
print (s)

s.insert(99)
print (s)

import time

t1 = time.time()
s.linked_reverse1()
t2 = time.time()
print (s,t2-t1)

t1 = time.time()
s.linked_reverse2()
t2 = time.time()
print (s, t2-t1)


q = Sll()
q.insert(9)
q.insert(9)
q.insert(8)
q.insert(9)
q.insert(9)
print (q)




q.increment1()
print (q, 'increment by 1')

q.increment()
print (q, 'increment by 1 another method')


n1= Sll()
n1.insert(9)
n1.insert(9)
n1.insert(9)
n1.insert(9)

n2= Sll()
#n2.insert(9)
#n2.insert(9)
n2.insert(9)

res = add(n1,n2)
print (res, 'add two linked list. Result will go to either first list or bigger list')

n1= Sll()
n1.insert(1)
n1.insert(2)
n1.insert(3)


n2= Sll()
n2.insert(7)
n2.insert(8)

reverse_add = 1
res = add(n1,n2)
print (res, 'add two linked list straight order. Result will go to either first list or bigger list')

n1= Sll()
n1.insert(1)
n1.insert(2)
n1.insert(3)


n2= Sll()
n2.insert(7)
n2.insert(8)

res = add(n1,n2, reverse_add)
print (res, 'add two linked list reverse order. Result will go to either first list or bigger list')


n3 = Sll()
n3.insert(1)
n3.insert(2)
n3.insert(3)
n3.insert(4)
n3.insert(5)
#print(n3)

# creating loop
print(n3.head.next_node.next_node.next_node.next_node.data)
print (n3.head.next_node.data)
n3.head.next_node.next_node.next_node.next_node.next_node = n3.head.next_node
print(n3.detectLoop())
print(n3.detectAndRemoveLoop())
print(n3)

# palindrome
n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(3)
n4.insert(4)
print(n4.firstSecondlargest())
print(n4)

n5 = Sll()
n5.insert(1)
n5.insert(2)
n5.insert(3)
n5.insert(4)
n5.insert(3)
n5.insert(2)
n5.insert(1)
print(n5)
print(n5.isPalindrome(),"plindrome ")
print(n5)

n4 = Sll()
n4.insert(3)
n4.insert(7)
n4.insert(2)
n4.insert(3)

n5 = Sll()
n5.insert(9)
n5.insert(8)
n5.insert(7)
print(n4)
print(n5)
s = addTwoNumbers(n4,n5)
print(s,"add two numbers")

n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(4)
n4.insert(5)

n5 = Sll()
n5.insert(1)
n5.insert(2)
n5.insert(3)
s= mergeTwoLists(n4,n5)
print(s,"merger two sorted lists")

n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(4)
n4.insert(5)
n4.insert(6)
n4.insert(7)
print(n4,"before swapped")
n4.swapPairs()
print(n4,'swapped')
n4.swapPairs2()
print(n4,'second swap')

# s = mergeTwoListsrecursive(n4.head,n5.head)
# while s:
#     print(s.data)
#     s= s.next_node

n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(4)
n4.insert(5)
n4.insert(6)
n4.insert(7)
print(n4)
n4.removeNthFromEnd(3)
print(n4,"remove 2 from last")


n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(4)
n4.insert(5)

n5 = Sll()
n5.insert(1)
n5.insert(2)
n5.insert(3)
n6 = Sll()
n6.insert(2)
n6.insert(4)
n6.insert(6)
n7 =Sll()
n7.insert(3)
n7.insert(5)
n7.insert(6)
n7.insert(7)
s= mergeKLists([n4,n5,n6,n7])
print(s,"merger k sorted lists")


n4 = Sll()
n4.insert(1)
n4.insert(2)
n4.insert(3)
n4.insert(4)
n4.insert(5)
n4.insert(6)
n4.insert(7)
n4.insert(8)
n4.insert(9)
n4.insert(10)
print(n4)
n4.reverseKGroup(3)
print(n4,"reverse nodes in k groups")




# 11->21->12->None
# 11->21->12->13->14->15->None 6
# 5
# Value not found Value found
# ('Value found at index', 5) Value not found
# 11->21->12->13->15->None 5
# 10->11->21->12->13->15->None
# 10->11->21->12->14->13->15->None
# 9->10->11->21->12->14->13->15->None 9
# 9->10->11->21->12->14->13->16->15->None
# 9->10->11->21->12->14->13->16->15->99->None
# 99->15->16->13->14->12->21->11->10->9->None 1.0013580322265625e-05
# 9->10->11->21->12->14->13->16->15->99->None 3.0994415283203125e-06
# 9->9->8->9->9->None
# 9->9->9->0->0->None increment by 1
# 9->9->9->0->1->None increment by 1 another method
# 1->0->0->0->8->None add two linked list. Result will go to either first list or bigger list
# 2->0->1->None add two linked list straight order. Result will go to either first list or bigger list
# 4->0->8->None add two linked list reverse order. Result will go to either first list or bigger list
# 5
# 2
# Found Loop
# found
# 1->2->3->4->5->None
# (4, 2)
# 1->2->3->4->None
# 1->2->3->4->3->2->1->None
# True plindrome
# 1->2->3->4->3->2->1->None
# 3->7->2->3->None
# 9->8->7->None
# 4->7->1->0->None add two numbers
# 1->1->2->2->3->4->5->None merger two sorted lists
# 1->2->4->5->6->7->None before swapped
# 2->1->5->4->7->6->None swapped
# 1->2->4->5->6->7->None second swap
# 1->2->4->5->6->7->None
# 1->2->4->6->7->None remove 2 from last
# 1->1->2->2->2->3->3->4->4->5->5->6->6->7->None merger k sorted lists
