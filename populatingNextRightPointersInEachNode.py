# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root and root.left and root.right:
        	root.left.next = root.right
        	rootLeft = self.connect(root.left)
        	rootRight = self.connect(root.right)
        	while rootLeft.right and rootRight.left:
        		rootLeft.right.next = rootRight.left
        		rootLeft = rootLeft.right
        		rootRight = rootRight.left
        return root