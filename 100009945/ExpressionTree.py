#  File: ExpressionTree.py

#  Description: Creates and evaluates an expression tree from an inputted infix expression; outputs postfix
#                and prefix notations for inputted infix expression

#  Student Name: Kalab Alemu

#  Student UT EID: kga469

#  Partner Name: Joseph Hendrix

#  Partner UT EID: jlh7459

#  Course Name: CS 313E

#  Unique Number: 52595

#  Date Created: 11/12/21

#  Date Last Modified: 11/12/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        dataStr = str(self.data)
        return dataStr


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        tree_stack = Stack()
        self.root = Node()
        curr = self.root
        expr = expr.split()
        for char in expr:
            # if left parenthesis
            if char == "(":
                tree_stack.push(curr)
                curr.lChild = Node()  # make it left child
                curr = curr.lChild  # update current node

            elif char in operators:
                curr.data = char
                tree_stack.push(curr)  # if char in list of operators
                curr.rChild = Node()  # push curr node onto stack
                curr = curr.rChild  # make node right child, update curr node

            elif char == ")":  # If right parenthesis
                if tree_stack.is_empty() == False:  # If stack is not empty
                    curr = tree_stack.pop()  # pop the stack to make curr node the parent node
                else:
                    break

            else:  # if the char is a digit
                curr.data = char  # update curr node to the digit
                curr = tree_stack.pop()  # pop the stack

    def evaluate(self, aNode):  # evaluate the expression
        if aNode.data == '+':
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        if aNode.data == '/':
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        if aNode.data == '*':
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        if aNode.data == '//':
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        if aNode.data == '%':
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        if aNode.data == '-':
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        if aNode.data == '**':
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else:
            return float(aNode.data)  # expression value returned

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        strExpr = self.preOrderHelp(aNode, [])
        return " ".join(strExpr)

    def preOrderHelp(self, aNode, s):
        if aNode is not None:
            s.append(aNode.data)
            self.preOrderHelp(aNode.lChild, s)
            self.preOrderHelp(aNode.rChild, s)
        return s

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        strExpr = self.postOrderHelp(aNode, [])
        return " ".join(strExpr)

    def postOrderHelp(self, aNode, s):
        if aNode is not None:
            self.postOrderHelp(aNode.lChild, s)
            self.postOrderHelp(aNode.rChild, s)
            s.append(aNode.data)
        return s

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
