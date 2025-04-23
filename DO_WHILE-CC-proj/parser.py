grammar = {
    'D': ['do { D | X | null } while (Expression);'],
    'X': ['D X', 'null']
}

# FIRST sets initialization
FIRST = {}
for key in grammar:
    FIRST[key] = set()

# FOLLOW sets initialization
FOLLOW = {}
for key in grammar:
    FOLLOW[key] = set()

def calculate_first(grammar, symbol):
    if symbol in FIRST[symbol]:
        return

    for production in grammar[symbol]:
        first_char = production.split()[0]

        if first_char.islower() or first_char.isdigit() or first_char == 'null':
            FIRST[symbol].add(first_char)
        elif first_char in grammar:
            calculate_first(grammar, first_char)
            FIRST[symbol] |= FIRST[first_char]

for symbol in grammar:
    calculate_first(grammar, symbol)

# Calculate FOLLOW sets
FOLLOW['D'].add('$')  # Adding end of input symbol

FOLLOW['D'] |= {'do'}  # Update follows based on grammar rules
FOLLOW['X'] |= {'$','do'}  # Update follows based on grammar rules

# Display FIRST sets
print("FIRST sets:")
for key, value in FIRST.items():
    print(f"{key}: {value}")

# Display FOLLOW sets
print("\nFOLLOW sets:")
for key, value in FOLLOW.items():
    print(f"{key}: {value}")

# Parse table initialization
parse_table = {}
for non_terminal in grammar:
    for terminal in FIRST[non_terminal]:
        if terminal != 'null':
            if terminal in grammar[non_terminal][0]:
                parse_table[(non_terminal, terminal)] = grammar[non_terminal][0]

# Handling X productions
for terminal in FOLLOW['X']:
    if terminal != '$':
        if terminal == 'do':
            parse_table[('X', terminal)] = 'D X | null'

parse_table[('X', '$')] = 'null'

# Display Parse Table
print("\nParse Table:")
for key, value in parse_table.items():
    print(f"{key}: {value}")

# Parse function
def parse_input(input_string):
    stack = ['$', 'D']  # Initialize stack with end of input symbol and start symbol
    input_string += '$'  # Append end of input symbol to the input string
    idx = 0

    # Display Parsing Steps
    print("\nParsing Steps:")
    while stack:
        print(f"\nStack: {' '.join(stack)}\tInput: {input_string[idx:]}")

        top = stack.pop()

        if top in grammar:
            if (top, input_string[idx]) in parse_table:
                production = parse_table[(top, input_string[idx])]
                for char in reversed(production.split()):
                    if char != 'null':
                        stack.append(char)
            else:
                return False
        elif top == input_string[idx]:
            if top == '$':
                return True
            idx += 1
        else:
            return False

    return False

input_str = 'do { do null } while (Expression);'

# Validate input string using the parser
result = parse_input(input_str)
if result:
    print("\nInput string is valid!")
else:
    print("\nInput string is not valid.")



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_expression(expression):
    tokens = list(expression.replace(" ", ""))  # Remove spaces and split characters
    root, _ = parse_E(tokens)
    return root

def parse_E(tokens):
    left_node, tokens = parse_T(tokens)
    while tokens and tokens[0] in '+-':
        op = tokens.pop(0)
        right_node, tokens = parse_T(tokens)
        new_node = Node(op)
        new_node.left = left_node
        new_node.right = right_node
        left_node = new_node
    return left_node, tokens

def parse_T(tokens):
    left_node, tokens = parse_F(tokens)
    while tokens and tokens[0] in '*/':
        op = tokens.pop(0)
        right_node, tokens = parse_F(tokens)
        new_node = Node(op)
        new_node.left = left_node
        new_node.right = right_node
        left_node = new_node
    return left_node, tokens

def parse_F(tokens):
    token = tokens.pop(0)
    if token.isdigit():
        return Node(f"Digit ({token})"), tokens
    # Add more rules if parentheses or other factors are needed
    raise ValueError("Invalid token")

def print_tree(node, level=0):
    if node:
        print(" " * (4 * level) + node.value)
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

# Example usage:
expression = "3 + 4 * 5"
root = parse_expression(expression)
print("Parse Tree:")
print_tree(root)


PARSER
class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())
        self.terminals = self.compute_terminals()
        self.first = {}
        self.follow = {}
        self.parse_table = {}

    def compute_terminals(self):
        terminals = set()
        for production in self.productions.values():
            for rule in production:
                for symbol in rule:
                    if symbol not in self.non_terminals and symbol != 'ε':
                        terminals.add(symbol)
        return terminals

    def compute_first(self):
        for non_terminal in self.non_terminals:
            self.first[non_terminal] = set()
        
        for non_terminal in self.non_terminals:
            self.compute_first_recursive(non_terminal)

    def compute_first_recursive(self, non_terminal):
        for production in self.productions[non_terminal]:
            first_symbol = production[0]
            if first_symbol not in self.non_terminals:
                self.first[non_terminal].add(first_symbol)
            elif first_symbol != non_terminal:
                self.compute_first_recursive(first_symbol)
                self.first[non_terminal].update(self.first[first_symbol])

    def compute_follow(self):
        for non_terminal in self.non_terminals:
            self.follow[non_terminal] = set()

        start_symbol = list(self.productions.keys())[0]
        self.follow[start_symbol].add('$')

        changed = True
        while changed:
            changed = False
            for non_terminal in self.non_terminals:
                for production in self.productions[non_terminal]:
                    for i, symbol in enumerate(production):
                        if symbol in self.non_terminals:
                            if i < len(production) - 1:
                                beta = production[i + 1:]
                                first_beta = self.compute_first_of_beta(beta)
                                if 'ε' in first_beta:
                                    first_beta.remove('ε')
                                    if self.update_follow_set(symbol, first_beta):
                                        changed = True
                            if i == len(production) - 1 or ('ε' in self.compute_first_of_beta(production[i + 1:])):
                                if self.update_follow_set(symbol, self.follow[non_terminal]):
                                    changed = True

    def compute_first_of_beta(self, beta):
        first_beta = set()
        for symbol in beta:
            if symbol in self.non_terminals:
                first_beta.update(self.first[symbol])
                if 'ε' not in self.first[symbol]:
                    break
            else:
                first_beta.add(symbol)
                break
        return first_beta

    def update_follow_set(self, non_terminal, new_follow_set):
        initial_size = len(self.follow[non_terminal])
        self.follow[non_terminal].update(new_follow_set)
        return len(self.follow[non_terminal]) != initial_size

    def construct_parse_table(self):
        for non_terminal in self.non_terminals:
            self.parse_table[non_terminal] = {terminal: [] for terminal in self.terminals}
            self.parse_table[non_terminal]['$'] = []

        for non_terminal in self.non_terminals:
            for production in self.productions[non_terminal]:
                first_set = self.compute_first_of_beta(production)
                for terminal in first_set:
                    if terminal != 'ε':
                        self.parse_table[non_terminal][terminal].append(production)
                
                if 'ε' in first_set or not first_set:
                    for terminal in self.follow[non_terminal]:
                        self.parse_table[non_terminal][terminal].append(production)
    
    def print_parse_table(self):
        headers = list(self.terminals) + ['$']
        print(f"{'':<5}", end='')
        for header in headers:
            print(f"{header:<10}", end='')
        print()

        for non_terminal, row in self.parse_table.items():
            print(f"{non_terminal:<5}", end='')
            for header in headers:
                production = row[header]
                production_str = ' | '.join([' '.join(prod) for prod in production])
                print(f"{production_str:<10}", end='')
            print()

def main():
    productions = {
        'S': [['do', '{', 'A', 'AB', '}', 'while', '(', ')']],
        'A': [['S'], ['S', 'A'], ['ε']],
        'B': [['A', 'B'], ['ε']]
    }

    grammar = Grammar(productions)
    grammar.compute_first()
    grammar.compute_follow()
    grammar.construct_parse_table()

    print("FIRST sets for non-terminals:")
    for non_terminal, first_set in grammar.first.items():
        if non_terminal in grammar.non_terminals:
            print(f"FIRST({non_terminal}) = {{ {', '.join(first_set)} }}")

    print("\nFOLLOW sets for non-terminals:")
    for non_terminal, follow_set in grammar.follow.items():
        print(f"FOLLOW({non_terminal}) = {{ {', '.join(follow_set)} }}")

    print("\nParse Table:")
    grammar.print_parse_table()

if __name__ == "__main__":
    main()

