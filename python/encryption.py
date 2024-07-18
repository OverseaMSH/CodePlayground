while True:
    print("Select an option:\n\t 1)Encrypt\n\t 2)Decrypt \n\t 3)Exit")
    selection = input("Your selection: ")
    if selection == "1":
        plainText = input("Enter your message: ")
        encryptedText=""
        for char in plainText:
            charCode= ord(char)*2+5
            encryptedText+=chr(charCode)
        print("Encrypted text :",encryptedText)
        print("\n"+"*"*40)

    elif selection == "2":
        encryptedText=input("Enter your message: ")
        plainText=""
        for char in encryptedText:
            charCode= (ord(char)-5)//2
            plainText+=chr(charCode)
        print("Plain text :",plainText)
        print("\n"+"*"*40)
    elif selection == "3":
        print("Goodbye")
        break
    else:
        print("Invalid selection")