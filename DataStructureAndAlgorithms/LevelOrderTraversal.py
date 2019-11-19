# This is another way of traversal in Binary Tree

# Level Order Traversal uses queues to hold intermediate tree nodes to perform the traversal

# Level Order Traversal is BFS for a tree

# Python has queue as a module in it whereas we use a list to act as a queue down here

# List as a stack is a perfect implementation as stack is LIFO and on a list append and pop operations take O(1) time

# List as a queue is a bit different as queue is FIFO and push and pop operations on LIST is O(n) because it needs to adjust element

# ... poistion by itself. To overcome that we would use Collections.dequeue

from collections import deque
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


def lot(root_node):
    current = root_node
    queue = deque([])
    queue.append(current)
    while True:
        if queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            print(node.data)

        else:
            break


lot(root)
