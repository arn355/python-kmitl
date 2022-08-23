class Stack:
    def __init__(self, ls = None):
        if ls == None:
            self.ls = []
        else:
            self.ls = list(ls)

    def push(self, i):
        self.ls.append(i)

    def pop(self):
        return self.ls.pop()

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        return False
    
    def size(self):
        return len(self.elements)

def postFixeval(st):
    s = Stack()
    for i in st:
        try:
            s.push(int(i))
        except ValueError:
            val1 = s.pop()
            val2 = s.pop()
            if i == '/':
                s.push(val2 / val1)
            else:
                operator ={'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '^':val2**val1}
                s.push(operator.get(i))

    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))