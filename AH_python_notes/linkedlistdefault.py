#linked list default
#basically the most basic of linked lists - singly
#next pointer is basically the next position it travels to yo 

import random 
letters = ['A','B','C','D','E','F','G']

from dataclasses import dataclass 

@dataclass
class node: #node is the compsci term for data structure thats floating in memory (space for data to be inserted(small part of a piece of data))
    data : str = ''
    nextPtr : int = -1 #pointer

def displayNode(thisNode):
    print(thisNode.data)
    if thisNode.nextPtr == -1:
        print("End of the list.")
    else:
        print("Going to this node next: ", thisNode.nextPtr)
        input()
        displayNode(singlyLinkedList[thisNode.nextPtr])

singlyLinkedList = [node() for x in range(10)]
for x in range(10):
    singlyLinkedList[x].data = random.choice(letters)
    singlyLinkedList[x].nextPtr = random.randint(0,9)
headPtr = 4 #starts at node position 4 
print(singlyLinkedList)
firstNode = singlyLinkedList[headPtr]
displayNode(firstNode)