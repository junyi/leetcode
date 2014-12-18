# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        l = []
        S = sorted(S)
        return self.solve(S, l)

    def solve(self, S, res):
        if S not in res:
            res.append(S)
            for s in S:
                S2 = S[:]
                S2.remove(s)
                self.solve(S2, res)
        return res

sol = Solution()
res = sol.subsetsWithDup([4,1,0])
print len(res), res
