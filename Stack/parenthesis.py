class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False
    
    def size(self):
        return len(self.elements)
    
def parenCheck(paren_in):
    left_paren = ['(', '[', '{']
    right_paren = [')', ']', '}']
    for i in paren_in:
        if i in left_paren:
            stack.push(i)
        elif i in right_paren:
            if stack.is_empty():
                return f'{paren_in} close paren excess'
            last = stack.peek()

            if right_paren.index(i) == left_paren.index(last):
                stack.pop()
            else:
                return f'{paren_in} Unmatch open-close'

    if stack.is_empty():
        return f'{paren_in} MATCH'
    return f'{paren_in} open paren excess   {stack.size()} : ' + ''.join(stack.elements)

stack = Stack()
paren_in = input("Enter expresion : ")
print(parenCheck(paren_in))

