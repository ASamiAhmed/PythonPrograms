text = input("Enter text: ")
consonantc= 0
vowelc = 0
for i in text:
    if (i=="a")or(i=="e")or(i=="i")or(i=="o")or (i=="u"):
        vowelc+=1
    elif (i==" "):
        print(end="")    
    else:
        consonantc+=1

print("occurence of vowels are",vowelc)
print("occurence of consonants are",consonantc)
