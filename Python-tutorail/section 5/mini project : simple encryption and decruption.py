while True:
    print("select your option\n\t1)encrypt\t2)decrypt\t3)exit")
    
    choice = input("your choice: ")
    
    if choice == "1":
        palin_text = input("text: ")
        encrypted_text = ""
        
        for c in palin_text:
            x = ((ord(c) * 34) // 2)
            encrypted_text += chr(x)
        
        print("encrypted text: ", encrypted_text)
        print("\n", "*"*30)  
    
    elif choice == "2":
        encrypted_text = input("text: ")
        palin_text = ""
        
        for e in encrypted_text:
            x = ((ord(e) * 2) // 34)
            palin_text += chr(x)
        
        print("palin_text: ", palin_text)
        print("\n", "*"*30)

    elif choice == "3":
        print("good bye!")
        print("\n")
        break
    
    else:
        print("choice is wraing")
        print("\n", "*"*30)

