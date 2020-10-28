# Linked List construction

#Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None/null. The class should support:
#   -Setting the head and tail of the linked list
#   -Inserting the nodes before and after the other nodes as well as at given positions (the position of the head node is 1)
#   -Removing given nodes and removing nodes with given values
#   -Searching for nodes with given values

#Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods all take in actuall Nodes as input parameters - not integers (except for insertAtPosition), which also takes in an interger representing the position); this means that you don't need to create any new Nodes in these methods. The input nodes can be either stand alone nodes or nodes that are already in the linked list. if they're nodes that are already in the linked list, the methods will effectively moving the nodes within the linked list. You wont be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario. 

#if you're doing this problem in an untyped language like Python or Javascript, you may want to look at the various function signatures ina  types language like Java or TypeScript to get a better idea of what each input parameter is.

#each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None/null

#Sample Usage:
#Assume the following linked list has already been created:
# 1, 2, 3, 4, 5
# Assume that we also have the following stand alone nodes:
#3, 3, 6

#setHead(4): 4, 1, 2, 3, 5 // set the exisiting node with value 4 as the head
#setTail(6): 4, 1, 2, 3, 5, 6 // set the stand alone node with the value 6 as the tail
#insertBefore(6, 3): 4, 1, 2, 5, 3, 6 // move the exisiting node with valye 3 before the exisiting node with value 6
#insertAfter(6,3): 4, 1, 2, 5, 3, 6, 3 // insert a stand-alone node with value 3 after the exisiting node with value 6
#insertAtPosition(1, 3): 3, 4, 1, 2, 5, 3, 6, 3 // insert a stand-alone node with value 3 in position 1
#removeNodesWithValue(3): 4, 1, 2, 5, 6 // remove all nodes with value 3
#remove(2): 4, 1, 5, 6 // //remnove the existing node with value 2
#containsNodeWithValue(5): true

# This is the input class
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, values):
        pass
    
    def remove(self, node):
        pass

    def containsNodeWithValue(self, value):
        pass
