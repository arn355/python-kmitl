print("*** Fun with countdown ***")
list_input = [int(x) for x in input("Enter List : ").split()]
list_re = list(reversed(list_input))
countdown = []

for i in range(0, len(list_re)):
    if(list_re[i] == 1):
        tmp = []
        index = i
        while index + 1 < len(list_re) and list_re[index] == list_re[index+1] - 1:
            tmp.append(list_re[index])
            index += 1
        tmp.append(list_re[index])
        countdown.append(list(reversed(tmp)))

print([len(countdown), list(reversed(countdown))])
