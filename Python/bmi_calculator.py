def bmi_calculate(h, w):
    return w/(h**2)

def check_bmi(bmi):
    if bmi < 18.5:
        return "Less Weight"
    elif bmi < 23:
        return "Normal Weight"
    elif bmi < 25:
        return "More than Normal Weight" 
    elif bmi < 30:
        return "Getting Fat"
    else:
        return "Fat"

data = [float(x) for x in input("Enter your High and Weight : ").split()]
checking = bmi_calculate(data[0], data[1])
print(check_bmi(checking))