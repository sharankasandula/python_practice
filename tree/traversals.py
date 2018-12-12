from tree import Node
from queue import Queue

inorderList = []
preorderList = []
postorderList = []
BFSList = []


def initializeTree():
    root = Node(1)
    root.leftNode = Node(2)
    root.rightNode = Node(3)
    root.leftNode.leftNode = Node(4)
    root.leftNode.rightNode = Node(5)
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


root = initializeTree()

inorderTraversal(root)
print("Inorder Travesal - ")
print(inorderList)

preorderTraversal(root)
print("Preorder Travesal - ")
print(preorderList)

postorderTraversal(root)
print("Postorder Travesal - ")
print(postorderList)

print (Queue)

breadthFirstSearch(root)
print("BFS Travesal - ")
print(BFSList)



            
    
