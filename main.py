class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.val, end=" ")
            self._inorder_traversal(node.right)

    def preorder_traversal(self):
        if self.root is not None:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.val, end=" ")
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.val, end=" ")

# Test
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
bst.inorder_traversal()
print("\nPreorder traversal:")
bst.preorder_traversal()
print("\nPostorder traversal:")
bst.postorder_traversal()
```

Bu kodda, `Node` klassi ikkilik daraxtning har bir nodini ifodalaydi. `BST` klassi ikkilik daraxtning umumiy xususiyatlarini ifodalaydi. `insert` metodi yangi nodni daraxtga qo'shadi, `inorder_traversal`, `preorder_traversal`, `postorder_traversal` metodi esa daraxtning ushbu tartiblarda bo'lishini ko'rsatadi.
