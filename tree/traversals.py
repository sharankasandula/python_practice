from tree import Node

inorderList = []
preorderList = []
postorderList = []


def initializeTree():
    root = Node(1)
    root.l = Node(2)
    root.r = Node(3)
    root.l.l = Node(4)
    root.l.r = Node(5)
    return root

def preorderTraversal(root):
    if root is None:
        return
    preorderList.append(root.v)
    preorderTraversal(root.l)
    preorderTraversal(root.r)


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.l)
    inorderList.append(root.v)
    inorderTraversal(root.r)


def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.l)
    postorderTraversal(root.r)
    postorderList.append(root.v)

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

