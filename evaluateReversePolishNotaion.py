# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
    	stack = []
        for token in tokens:
        	if token in ['+', '-', '*', '/']:
        		opB = stack.pop()
        		opA = stack.pop()
        		if token == '+':
        			res = opA + opB
        		elif token == '-':
        			res = opA - opB
        		elif token == '*':
        			res = opA * opB
        		elif token == '/':
        			res = opA / float(opB)
        		stack.append(int(res))
        	else:
        		stack.append(int(token))
        return stack.pop()

exp1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print sol.evalRPN(exp1)