def hbd(age):
    ### Enter Your Code Here ###
    if age % 2 == 0:
        result = f'saimai is just 20, in base {age//2}!'
    else:
        result = f'saimai is just 21, in base {age//2}!'
    return result

year = input("Enter year : ")

print(hbd(int(year)))