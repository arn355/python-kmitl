class Calculator :

    ### Enter Your Code Here ###
    def __init__(self, x) -> None:
        self.x = x

    def __add__(self, obj):
        return self.x + obj.x
        ###Enter Your Code For Add Number###

    def __sub__(self, obj):
        return self.x - obj.x
        ###Enter Your Code For Sub Number### 

    def __mul__(self, obj):
        return self.x * obj.x
        ###Enter Your Code For Mul Number###

    def __truediv__(self, obj):
        return self.x / obj.x
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")