#12
class EarleyItem:
    def __init__(self, production, dot_position, start_column):
        self.production = production
        self.dot_position = dot_position
        self.start_column = start_column

def predict(grammar, column, item):
    non_terminal = item.production[item.dot_position]
    for rule in grammar.get(non_terminal, []):
        new_item = EarleyItem(rule, 0, column)
        if new_item not in column:
            column.append(new_item)

def scan(tokens, column, item):
    if item.dot_position < len(tokens) and \
       item.production[item.dot_position] == tokens[column]:
        new_item = EarleyItem(item.production, item.dot_position + 1, item.start_column)
        if new_item not in column:
            column.append(new_item)

def complete(chart, column, item):
    for entry in chart[item.start_column]:
        if entry.dot_position < len(entry.production) and \
           entry.production[entry.dot_position] == item.production and \
           EarleyItem(entry.production, entry.dot_position + 1, entry.start_column) not in chart[column]:
            chart[column].append(EarleyItem(entry.production, entry.dot_position + 1, entry.start_column))

def earley_parse(tokens, grammar):
    chart = {i: [] for i in range(len(tokens) + 1)}
    start_rule = list(grammar.keys())[0]
    chart[0].append(EarleyItem(start_rule, 0, 0))

    for column in range(len(tokens) + 1):
        for item in chart[column]:
            if item.dot_position < len(item.production) and \
               isinstance(item.production[item.dot_position], str):
                scan(tokens, column, item)
            elif item.dot_position < len(item.production):
                predict(grammar, chart[column], item)
            else:
                complete(chart, column, item)

    for item in chart[len(tokens)]:
        if item.production == [start_rule] and item.dot_position == 1 and item.start_column == 0:
            return False

    return True

# Example usage:
example_grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog'],
    'V': ['chased', 'ate']
}

example_tokens = ['the', 'dog', 'chased', 'a', 'cat']

result = earley_parse(example_tokens, example_grammar)
print("Parsing successful:", result)
