# simple binary tree data structure
class Tree:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


    def inorder(self):
        traversal = []

        def inorder_aux(tree, current):
            if tree.left != None:
                inorder_aux(tree.left, current)

            current.append(tree.data)

            if tree.right != None:
                inorder_aux(tree.right, current)


        inorder_aux(self, traversal)

        return traversal


    def preorder(self):
        traversal = []

        def preorder_aux(tree, current):
            current.append(tree.data)

            if tree.left != None:
                preorder_aux(tree.left, current)
            if tree.right != None:
                preorder_aux(tree.right, current)

        preorder_aux(self, traversal)

        return traversal


    def postorder(self):
        traversal = []

        def postorder_aux(tree, current):
            if tree.left != None:
                postorder_aux(tree.left, current)
            if tree.right != None:
                postorder_aux(tree.right, current)

            current.append(tree.data)

        postorder_aux(self, traversal)

        return traversal

