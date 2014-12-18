# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        # print root.val , self.greedyMaxPath(root.left), self.greedyMaxPath(root.right)
        return self.maxPathSolve(root)

    def maxPathSolve(self, root):
        if root:
            tempMax = root.val
            leftMaxPath = 0
            rightMaxPath = 0
            if root.left:
                tempMax += self.greedyMaxPath(root.left)
                leftMaxPath = self.maxPathSolve(root.left)
            if root.right:
                tempMax += self.greedyMaxPath(root.right)
                rightMaxPath = self.maxPathSolve(root.right)
            print tempMax, leftMaxPath, rightMaxPath
            return max(tempMax, leftMaxPath, rightMaxPath)
        else:
            return 0


    def greedyMaxPath(self, root):
        if root and not root.left and not root.right:
            return root.val
        elif root:
            leftMax = self.greedyMaxPath(root.left)
            rightMax = self.greedyMaxPath(root.right)
            return root.val + max(leftMax, rightMax)
        else:
            return 0

root = TreeNode(0)

t1 = TreeNode(2)
t1.left = TreeNode(3)
t1.right = TreeNode(10)

t2 = TreeNode(3)
t2.right = TreeNode(17)

t3 = TreeNode(1)
t3.left = t1
t3.right = t2

t4 = TreeNode(1)
t4.left = TreeNode(10)

t5 = TreeNode(2)
t5.left = t4
t5.right = TreeNode(5)

root.left = t3
root.right = t5

sol = Solution()
print sol.maxPathSum(root)