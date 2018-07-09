
prefix_expr = '+ * 2 3 1'

def evaluate(expr):
	expr_list = expr.split()
	val, idx = evaluate_rec(expr_list, 0)
	return val

def evaluate_rec(expr, i):
	if expr[i] == '+':
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return a + b, i
	elif expr[i] == '-':
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return a - b, i
	elif expr[i] == '*':
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return a * b, i
	elif expr[i] == '/':
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return a / b, i
	else:
		return int(expr[i]), i + 1

import operator
operator_table = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv, # The '/'' operator. 
	                       # The '//'' operator is floordiv
}

def evaluate_rec(expr, i):
	print(expr[i])
	if expr[i] in ('+', '-', '*', '/'):
		op = operator_table[expr[i]]
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return op(a, b), i
	else:
		return int(expr[i]), i + 1


print(evaluate(prefix_expr))


## Infix
