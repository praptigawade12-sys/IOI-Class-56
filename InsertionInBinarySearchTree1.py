class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root,key):
    if root is None:
        return Node(key)

    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
        return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,80)

inorder(root)