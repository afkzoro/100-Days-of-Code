alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(pl_ciph, move, choice):
    cipher_text = ""

    
    for i in range(len(pl_ciph)):
        if pl_ciph[i] in alphabet:
            
            if choice == "encode":
                ind = alphabet.index(pl_ciph[i])
                cipher_text += alphabet[ind + move]

                
            elif choice == "decode":
                ind = alphabet.index(pl_ciph[i])
                cipher_text += alphabet[ind - move]
                
        elif pl_ciph[i] == " ":
            cipher_text += " " 
        else:
            cipher_text += pl_ciph[i]

    if choice == "encode":
        print(f"The encoded text is {cipher_text}")
    elif choice == "decode":
        print(f"The decoded text is {cipher_text}")
                    

caeser(pl_ciph=text, move=shift, choice=direction)
