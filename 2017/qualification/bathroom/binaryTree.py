class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:

    def __init__(self):
        self.root = None


    def insert_node(self,root,element):
        if self.root is None:
            self.root = Node(element)
        else:

            if root is None:
                root = Node(element)
            elif root.data <= element:
                root.right = self.insert_node(root.right,element)
            elif root.data > element:
                root.left = self.insert_node(root.left,element)


        return root

    def PreOrder(self,root):
        if root is not None:
            print(root.data)
            if root.left is not None:
                self.PreOrder(root.left)
            if root.right is not None:
                self.PreOrder(root.right)

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

    def inOrderTranversal(self, root):
        if root is not None:
            self.inOrderTranversal(root.left)
            print(root.data)
            self.inOrderTranversal(root.right)




a = BinaryTree()
a.insert_node(a.root,1)
a.insert_node(a.root,2)
a.insert_node(a.root,3)
a.insert_node(a.root,4)
a.insert_node(a.root,5)
a.insert_node(a.root,6)
a.insert_node(a.root,7)
a.insert_node(a.root,7)
a.insert_node(a.root,8)
a.insert_node(a.root,9)
a.insert_node(a.root,10)
a.insert_node(a.root,11)
a.insert_node(a.root,12)
a.insert_node(a.root,13)
a.insert_node(a.root,14)

print('\npreOrder')
a.PreOrder(a.root)

print('\ninOrderTranversal')
a.inOrderTranversal(a.root)

print('\npostOrder')
a.postOrder(a.root)