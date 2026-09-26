# infix_to_postfix.py

class Stack:
    def __init__(self):
        self.table = []                   # internal list to store elements
        self.content = 0                  # number of elements in the stack

    def createStack(self):
        self.table = []                   # initialize as empty stack
        self.content = 0
    
    def push(self, new):
        self.table.append(new)            # add element to top
        self.content += 1

    def pop(self):
        if self.content == 0:             # check if empty before popping
            return None
        self.content -= 1
        return self.table.pop()           # remove and return top element

    def peek(self):
        if self.content == 0:             # check if empty before peeking
            return None
        return self.table[-1]             # return top element without removing it

    def isEmpty(self):
        return self.content == 0          # True if stack is empty
    
    def deleteStack(self):
        self.table = []                   # clear all elements
        self.content = 0
        
    def show(self):
        return self.table                 # return stack contents


# ---------- TOKENIZER FUNCTION ----------
# Converts expression string into a list of operands, operators, and parentheses.
def tokenize(expr: str): #ab + 7a - c -> ["ab", "+", "7a", "-", "c"]
    """Split the given infix expression into small meaningful parts (tokens)."""
    tokens, i = [], 0                     # tokens = list of separated parts, i = current index

    while i < len(expr):                  # loop through the expression
        ch = expr[i]                      # get the current character

        if ch.isspace():                  # skip spaces (ignore them)
            i += 1
            continue

        if ch.isalnum():                  # if letter or number (operand)
            j = i                         # mark start of operand
            while j < len(expr) and expr[j].isalnum():   # continue while next chars are also alphanumeric
                j += 1
            tokens.append(expr[i:j])      # add full operand (like 'A', 'x1', '123')
            i = j                         # move index to end of operand
        else:
            tokens.append(ch)             # operator or parenthesis added as single token
            i += 1                        # move to next character

    return tokens                         # return final list of tokens


# ---------- INFIX TO POSTFIX CONVERSION ----------
PRECEDENCE = { '^': 3, '*': 2, '/': 2, '+': 1, '-': 1 }  # define operator precedence

def is_operator(tok: str) -> bool:
    return tok in PRECEDENCE              # returns True if token is an operator

def infix_to_postfix(expression: str) -> str:
    """Implements the infix → postfix algorithm based on stack rules (a–d)."""
    s = Stack()                           # create a new stack
    s.createStack()
    out = []                              # output list for postfix result

    for tok in tokenize(expression):      # process each token from left to right

        if tok.isalnum():                 # (a) If token is operand → print (append)
            out.append(tok)

        elif tok == '(':                  # (b) If token is '(' → push to stack
            s.push(tok)

        elif tok == ')':                  # (c) If token is ')' → pop until '('
            while not s.isEmpty() and s.peek() != '(':
                out.append(s.pop())       # pop and add operators to output
            s.pop()                       # discard '('

        elif is_operator(tok):            # (d) If token is operator
            while (not s.isEmpty() and s.peek() != '(' and
                   PRECEDENCE[s.peek()] >= PRECEDENCE[tok]):
                out.append(s.pop())       # pop operators of greater or equal precedence
            s.push(tok)                   # push current operator

    while not s.isEmpty():                # pop remaining operators
        out.append(s.pop())

    return " ".join(out)                  # return postfix expression as string


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("=== INFIX → POSTFIX CONVERTER (USING STACK) ===")
    examples = [
        "A+ B/C* D -E / (F + G)",
        "3+5*(5/5)-2^2"
    ]

    for expr in examples:
        print(f"Infix:   {expr}")
        print(f"Postfix: {infix_to_postfix(expr)}")
        print("-" * 35)

    # user input section
    user = input("Enter an infix expression: ")
    print("Postfix:", infix_to_postfix(user))

    #7+5*3/5^1+(3-2)
    #753*51^/+32-+
