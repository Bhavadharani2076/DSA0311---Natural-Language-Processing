#11
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def parse(self):
        return self.expr()

    def expr(self):
        result = self.term()

        while self.current_token in ('+', '-'):
            operator = self.current_token
            self.advance()
            right = self.term()
            if operator == '+':
                result += right
            elif operator == '-':
                result -= right

        return result

    def term(self):
        result = self.factor()

        while self.current_token in ('*', '/'):
            operator = self.current_token
            self.advance()
            right = self.factor()
            if operator == '*':
                result *= right
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result /= right

        return result

    def factor(self):
        token = self.current_token
        self.advance()

        if token == '(':
            result = self.expr()
            if self.current_token != ')':
                raise SyntaxError("Expected closing parenthesis")
            self.advance()
            return result
        elif token.isdigit():
            return int(token)
        else:
            raise SyntaxError("Invalid syntax")


def parse_input(input_string):
    tokens = input_string.replace(' ', '').replace('\t', '').split(',')
    parser = Parser(tokens)
    return parser.parse()

input_string = '5, *, (, 3, +, 7,), +, 10'
result = parse_input(input_string)
print(f"Result: {result}")
