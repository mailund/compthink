
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
	if expr[i] in ('+', '-', '*', '/'):
		op = operator_table[expr[i]]
		a, i = evaluate_rec(expr, i + 1)
		b, i = evaluate_rec(expr, i)
		return op(a, b), i
	else:
		return int(expr[i]), i + 1


print(evaluate(prefix_expr))


## Infix
def tokenise(expr):
	for op in ("(", ")", "+", "-", "*", "/"):
		expr = expr.replace(op, " " + op + " ")
	return expr.split()

def evaluate(expr):
	expr_list = tokenise(expr)
	val, idx = evaluate_rec(expr_list, 0)
	return val

def evaluate_rec(expr, i):
	if expr[i] == '(':
		a, i = evaluate_rec(expr, i + 1)
		op = operator_table[expr[i]]
		b, i = evaluate_rec(expr, i + 1)
		return op(a, b), i + 1 # + 1 to get past the ')'
	else:
		return int(expr[i]), i + 1

print("infix")
print(evaluate('12'))
print(evaluate('(2 + 3)'))
print(evaluate('((2 + 2) * 3)'))


# EXP  := OPEXP | LEXP
# OPEX := LEXP op EXP
# LEXP := PEXP | number
# PEXP := '(' EXP ')'

class ParseError(Exception):
	pass

def evaluate_exp(expr, i):
	try:
		return evaluate_opex(expr, i)
	except:
		return evaluate_lexp(expr, i)

def evaluate_opex(expr, i):
	lhs, i = evaluate_lexp(expr, i)
	op = operator_table[expr[i]] ; i += 1
	rhs, i = evaluate_exp(expr, i)
	return op(lhs, rhs), i

def evaluate_lexp(expr, i):
	try:
		return evaluate_pexp(expr, i)
	except:
		return int(expr[i]), i + 1

def evaluate_pexp(expr, i):
	if expr[i] != '(':
		raise ParseError
	val, i = evaluate_exp(expr, i + 1)
	if expr[i] != ')':
		raise ParseError
	return val, i + 1

def evaluate(expr):
	try:
		expr_list = tokenise(expr)
		val, idx = evaluate_exp(expr_list, 0)
		return val
	except:
		raise ParseError



print("infix 2")
print(evaluate('12'))
print(evaluate('(12)'))
print(evaluate('(2 + 3)'))
print(evaluate('2 + 3 + 4'))
print(evaluate('((2 + 2) * 3)'))

print(evaluate('(2+2)5'))
