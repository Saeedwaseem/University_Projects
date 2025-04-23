import re

path = "C:/Users/Dell/Documents/parsertask.txt"
f = open(path, 'r')
Buffer = f.read()

keywords2 = []
operators2 = []
special_characters2 = []
identifiers2 = []
numbers2 = []
Errors = []

operators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
keywords = ['break', 'case', 'char', 'do', 'double', 'else', 'float', 'for', 'goto', 'if',
            'int', 'long', 'return', 'short', 'static', 'switch', 'void', 'while']
special_characters = [' ', '\t', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']

tok = []
Str = False
Word = False
Cmt = 0
token = ''

for i in Buffer:
    if i == '/':
        Cmt = Cmt + 1

    elif Cmt == 2:
        if i == '\n':
            token = ''
            Cmt = 0

    elif i == '"' or i == "'":
        if Str:
            tok.append(token)
            token = ''
        Str = not Str

    elif Str:
        token = token + i

    elif i.isalnum() and not Word:  # position of a new word check
        Word = True
        token = i

    elif (i in special_characters) or (i in operators):
        if token:
            tok.append(token)
            token = ''

        if not (i == ' ' or i == '\n' or i == '\t'):
            tok.append(i)

    elif Word:
        token = token + i

for token in tok:
    if token in operators and token not in operators2:
        operators2.append(token)

    elif token in keywords and token not in keywords2:
        if token == 'do' or token == 'while':
            keywords2.append(token)
        else:
            Errors.append(token)

    elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$", token) and token not in identifiers2:
        identifiers2.append(token)

    elif token in special_characters and token not in special_characters2:
        special_characters2.append(token)

    elif re.search(r'\d+', token) and token not in numbers2:
        numbers2.append(token)

# Creating symbol table
symbol_table = []

index = 0  # Starting index value

for lexeme in keywords2:
    symbol_table.append((index, 'keywords', lexeme))
    index += 1

for lexeme in operators2:
    symbol_table.append((index, 'operators', lexeme))
    index += 1

for lexeme in identifiers2:
    symbol_table.append((index, 'identifiers', lexeme))
    index += 1

for lexeme in numbers2:
    symbol_table.append((index, 'numbers', lexeme))
    index += 1

for lexeme in special_characters2:
    symbol_table.append((index, 'special characters', lexeme))
    index += 1

for lexeme in Errors:
    symbol_table.append((index, 'errors', lexeme))
    index += 1

print("Symbol Table:")
print("(Index, Category, Lexeme)")
for entry in symbol_table:
    print(entry)

f.close()
import re

path = "C:/Users/Dell/Documents/parsertask.txt"
f = open(path, 'r')
Buffer = f.read()

keywords2 = []
operators2 = []
special_characters2 = []
identifiers2 = []
numbers2 = []
Errors = []

operators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
keywords = ['break', 'case', 'char', 'do', 'double', 'else', 'float', 'for', 'goto', 'if',
            'int', 'long', 'return', 'short', 'static', 'switch', 'void', 'while']
special_characters = [' ', '\t', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']

tok = []
Str = False
Word = False
Cmt = 0
token = ''

for i in Buffer:
    if i == '/':
        Cmt = Cmt + 1

    elif Cmt == 2:
        if i == '\n':
            token = ''
            Cmt = 0

    elif i == '"' or i == "'":
        if Str:
            tok.append(token)
            token = ''
        Str = not Str

    elif Str:
        token = token + i

    elif i.isalnum() and not Word:  # position of a new word check
        Word = True
        token = i

    elif (i in special_characters) or (i in operators):
        if token:
            tok.append(token)
            token = ''

        if not (i == ' ' or i == '\n' or i == '\t'):
            tok.append(i)

    elif Word:
        token = token + i

for token in tok:
    if token in operators and token not in operators2:
        operators2.append(token)

    elif token in keywords and token not in keywords2:
        if token == 'do' or token == 'while':
            keywords2.append(token)
        else:
            Errors.append(token)

    elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$", token) and token not in identifiers2:
        identifiers2.append(token)

    elif token in special_characters and token not in special_characters2:
        special_characters2.append(token)

    elif re.search(r'\d+', token) and token not in numbers2:
        numbers2.append(token)

# Creating symbol table
symbol_table = []

index = 0  # Starting index value

for lexeme in keywords2:
    symbol_table.append((index, 'keywords', lexeme))
    index += 1

for lexeme in operators2:
    symbol_table.append((index, 'operators', lexeme))
    index += 1

for lexeme in identifiers2:
    symbol_table.append((index, 'identifiers', lexeme))
    index += 1

for lexeme in numbers2:
    symbol_table.append((index, 'numbers', lexeme))
    index += 1

for lexeme in special_characters2:
    symbol_table.append((index, 'special characters', lexeme))
    index += 1

for lexeme in Errors:
    symbol_table.append((index, 'errors', lexeme))
    index += 1

print("Symbol Table:")
print("(Index, Category, Lexeme)")
for entry in symbol_table:
    print(entry)

f.close()
