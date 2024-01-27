#18
from pyparsing import Word, alphas, alphanums, Forward, infixNotation, opAssoc
identifier = Word(alphas, alphanums+"_")
and_op = "AND"
or_op = "OR"
implies_op = "IMPLIES"
not_op = "NOT"
expr = Forward()
atom = identifier | "(" + expr + ")"
term = infixNotation(atom, [
    (not_op, 1, opAssoc.RIGHT),
    (and_op, 2, opAssoc.LEFT),
    (or_op, 2, opAssoc.LEFT),
    (implies_op, 2, opAssoc.RIGHT),
])
def parse_expression(expression):
    return term.parseString(expression, parseAll=True)
logical_expression = "P AND (Q OR NOT R) IMPLIES S"
parsed_expr = parse_expression(logical_expression)
print(parsed_expr)
