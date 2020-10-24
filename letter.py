#Write a Python program to test whether a passed letter is a vowel or not
letter = input("Enter letter: ")
for i in letter:
    if (i=="a")or(i=="e")or(i=="i")or(i=="o")or(i=="u"):
        print("The letter you entered is vowel")
    else:
        print("The letter you entered is not vowel")    