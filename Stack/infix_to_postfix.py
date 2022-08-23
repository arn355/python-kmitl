class Stack:
    def __init__(self, list = None):
        if list == None:
            self.list = []
        else:
            self.list = list(list)

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False
    
    def size(self):
        return len(self.list)

def isOperand(ch): 
    return ch.isalpha()

def notGreater(stack ,i):
    precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
    if stack.peek() == '(':
        return False
    a = precedence[i]
    b = precedence[stack.peek()] 
    if a  <= b:
        return True
    else:
        return False

def infix2postfix(exp):
    output = ''
    s = Stack()

    for i in exp:
        if isOperand(i) == True:
            output += i

        elif i  == '(':
            s.push(i)

        elif i == ')':
            while(s.is_empty() != True and s.peek() != '('):
                val = s.pop() 
                output += val
            if (s.is_empty() != True and s.peek() != '('):
                return -1
            else:
                s.pop()
        else: 
            while(s.is_empty() != True and notGreater(s, i)):
                val = s.pop()
                output += val
            s.push(i)
 
    while s.is_empty() != True:
        val = s.pop()
        output += val
    
    return output
           
print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))