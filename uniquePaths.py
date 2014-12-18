# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 3 x 7 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

class Solution:
    # @return an integer
    cache = dict()
    def uniquePaths(self, m, n):
    	if n==1:
    		return 1
    	elif m==1:
    		return 1
    	else:
    		if (m - 1, n) in self.cache:
    			x = self.cache[(m-1, n)]
    		else:
    			x = self.uniquePaths(m-1, n)
    			self.cache[(m-1, n)] = x

    		if (m, n-1) in self.cache:
    			y = self.cache[(m, n-1)]
    		else:
    			y = self.uniquePaths(m, n-1)
    			self.cache[(m, n-1)] = y

        return x+y

sol = Solution()
print sol.uniquePaths(1, 10)
