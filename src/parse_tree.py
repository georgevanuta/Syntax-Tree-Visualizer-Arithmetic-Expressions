from misc import split_arith_expr
from tree import Tree


class ArithParseTree:
    def __init__(self, arith_expr):
        expr = split_arith_expr(arith_expr)
        stack = []
        self.tree = Tree()
        currentNode = self.tree
        stack.append(currentNode)

        for ch in expr:
            if ch == '(':
                currentNode.left = Tree()
                stack.append(currentNode)
                currentNode = currentNode.left
            elif ch in ['+', '-', '*', '/']:
                currentNode.data = ch
                currentNode.right = Tree()
                stack.append(currentNode)
                currentNode = currentNode.right
            elif ch == ')':
                currentNode = stack.pop()
            else:
                currentNode.data = ch
                currentNode = stack.pop()


    def get_expression(self):
        return "".join(self.tree.inorder())