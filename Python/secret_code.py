def bon(w):
	### Enter Your Code Here ###
    for i in w:
        if w.count(i) > 1:
            secret = (ord(i) - 96) * 4
    return secret
    
secretCode = input("Enter secret code : ")
print(bon(secretCode))