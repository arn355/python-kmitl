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

stack = Stack()
command_input = input("Enter Input : ").split(",")

for i in command_input:
    val_input = i.split()
    if val_input[0] == 'A':
        stack.push(val_input[1])
        print(f'Add = {stack.peek()} and Size = {stack.size()}')
    elif val_input[0] == 'P':
        if stack.is_empty():
            print("-1")
        else:
            index = stack.size() - 1
            val_pop = stack.pop()
            print(f'Pop = {val_pop} and Index = {index}')

if stack.is_empty():
    print("Value in Stack = Empty")
else:
    print("Value in Stack = ", end="")
    for val in stack.elements:
        print(val, end=" ")
