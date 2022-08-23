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

def pass_tree(h):
    stack.push(int(h))

def look_back():
    if stack.is_empty():
        count = 0
    else: 
        count = 1
    current_h = stack.peek()
    for i in range(-1, -stack.size() - 1, -1):
        if current_h < stack.elements[i]:
            count += 1
            current_h = stack.elements[i]
    print(count)

def drunk():
    tmp = []
    while not stack.is_empty():
        tree_h = stack.pop()
        if tree_h % 2 == 0:
            tmp.append(tree_h - 1)
        else:
            tmp.append(tree_h + 2)
   
    for tree in reversed(tmp):
        stack.push(tree)

def walking(inp):
    for i in inp:
        comm = i.split()
        if comm[0] == 'A':
            pass_tree(comm[1])
        elif comm[0] == 'B':
            look_back()
        else:
            drunk()

stack = Stack()
inp = input("Enter Input : ").split(",")
walking(inp)
