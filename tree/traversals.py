from tree import Node
from queue import Queue
import sys

inorderList = []
preorderList = []
postorderList = []
BFSList = []


def initializeTree():
    root = Node(10)
    root.leftNode = Node(5)
    root.rightNode = Node(15)
    root.leftNode.leftNode = Node(3)
    root.leftNode.rightNode = Node(7)
    root.rightNode.leftNode = Node(12)
    root.rightNode.rightNode = Node(18)
    return root


def preorderTraversal(root):
    if root is None:
        return
    preorderList.append(root.value)
    preorderTraversal(root.leftNode)
    preorderTraversal(root.rightNode)


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.leftNode)
    inorderList.append(root.value)
    inorderTraversal(root.rightNode)


def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.leftNode)
    postorderTraversal(root.rightNode)
    postorderList.append(root.value)


def breadthFirstSearch(root):
    # print (root)
    if root is None:
        return 
    q = Queue()

    q.enqueue(root)


    while not q.is_empty():
        currentNode = q.dequeue()
        BFSList.append(currentNode.value)
        if currentNode.leftNode is not None:
            q.enqueue(currentNode.leftNode)
        if currentNode.rightNode is not None:  
            q.enqueue(currentNode.rightNode)

def isBST(root, lowerBound, upperBound):
    if root is None:
        return True
    if root.value < lowerBound or root.value > upperBound:
        print("Your BST is wrong, b*tch. try again!")
        return False
    return isBST(root.leftNode, lowerBound, root.value) and isBST(root.rightNode, root.value, upperBound)



root = initializeTree()

inorderTraversal(root)
print("\nInorder Travesal ")
print(inorderList)

preorderTraversal(root)
print("\nPreorder Travesal ")
print(preorderList)

postorderTraversal(root)
print("\nPostorder Travesal ")
print(postorderList)


breadthFirstSearch(root)
print("\nBFS Travesal ")
print(BFSList)

#used sys.maxsize size because root node can practically have a value from -infinity to infinity
if isBST(root, -sys.maxsize-1, sys.maxsize):
    print("\nIts a valid BST")
else:
    print("\nIts not a valid BST. Piss off")
            
    
