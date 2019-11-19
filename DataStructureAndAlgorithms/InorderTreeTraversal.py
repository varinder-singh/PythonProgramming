# This program explains how to do Inorder Binary tree traversal in python

# By inorder we understand LDR - which is the abbrevation of Left -> Data -> Right node.

# let us first create our tree and then do the traversal

# This is inorder iterative


from BinaryTrees import BinaryTreeNode

root = BinaryTreeNode()
root.data = 1
root.left = BinaryTreeNode()
root.right = BinaryTreeNode()

first_left_node = root.left
first_right_node = root.right

first_left_node.data = 2
first_left_node.left = BinaryTreeNode()
first_left_node.right = BinaryTreeNode()

first_right_node.right = 3
first_right_node.left = BinaryTreeNode()
first_right_node.right = BinaryTreeNode()

first_left_node.left.data = 4
# first_left_node.left.left = BinaryTreeNode()
# first_left_node.left.right = BinaryTreeNode()

first_left_node.right.data = 5
# first_left_node.right.left = BinaryTreeNode()
# first_left_node.right.right = BinaryTreeNode()

first_right_node.left.data = 6
# first_right_node.left.left = BinaryTreeNode()
# first_right_node.left.right = BinaryTreeNode()

first_right_node.right.data = 7
# first_right_node.right.left = BinaryTreeNode()
# first_right_node.right.right = BinaryTreeNode()

if root:
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right

        else:
            break





