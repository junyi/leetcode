# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False
            
z = TreeNode(3)
z.left = TreeNode(4)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = z

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
print sol.isSameTree(p, q)