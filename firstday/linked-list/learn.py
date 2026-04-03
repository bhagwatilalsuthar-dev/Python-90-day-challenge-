class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
firstNode = Node(1)
secondNode = Node(2)
thirdNode=Node(3)
fourthNode=Node(4)
fiveNode=Node(5)
sixNode=Node(6)
sevenNode=Node(7)
eightNode=Node(8)
nineNode=Node(9)
tenNode=Node(10)


firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = fiveNode
fiveNode.next = sixNode
sixNode.next = sevenNode
sevenNode.next = eightNode
eightNode.next = nineNode
nineNode.next = tenNode
tenNode.next = None


def traversal(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print(currentNode)

def addNewValue(head):
    currentNode=head
    while currentNode.data <4:
        # print(currentNode.data)
        currentNode=currentNode.next
    tamp=currentNode.next #4
    elevenNode=Node(11) #-11
    currentNode.next=elevenNode
    elevenNode.next=tamp 


    
    return head
# ans=addNewValue(firstNode)
# traversal(ans)




class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None
    def insert_first(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    def insert_last(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        # print("None")
    # myList = LinkedList()
    # myList.insert_first(10)
    # myList.insert_first(5)
    # myList.insert_last(20)
    # myList.insert_last(30)
    # myList.display()



def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

ans=length_of_longest_substring("abcabcbb")
# print(ans)




def printNumber(x):
    myNewValue=int(x**0.5)
    for each in range(2,myNewValue+1):
     
     if(x%each==0):
        print(each,myNewValue)
        return False
    return True
     

# ans=printNumber(18)
# print(ans)
















import numpy as np
A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
result=np.dot(A,B)
# print(result)