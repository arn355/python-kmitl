def digit_sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

print(" *** Summation of each digit ***")
num = input("Enter a positive number : ")
sum = digit_sum(list(num))
print("Summation of each digit = ", sum)