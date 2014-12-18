# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Need to cache old result to avoid recalculation

class Solution:
    # @param n, an integer
    # @return an integer
    cache = dict()
    def climbStairs(self, n):
    	if n <= 2:
    		return n
    	else:
    		if n-1 in self.cache:
    			x = self.cache[n-1]
    		else:
    			x = self.climbStairs(n-1)
    			self.cache[n-1] = x

    		if n-2 in self.cache:
    			y = self.cache[n-2]
    		else:
    			y = self.climbStairs(n-2)
    			self.cache[n-2] = y
    		return x + y

sol = Solution()
print sol.climbStairs(35)