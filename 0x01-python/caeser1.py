alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, move):
    cipher_text = []
    for i in range(len(plain_text)):
        if plain_text[i] in alphabet:
            ind = alphabet.index(plain_text[i]) #Gets index of letter in the alphabet list
            
            cipher_text.append(alphabet[ind + move])
            
    print(f"{''.join(cipher_text)}")
encrypt(plain_text=text, move=shift)


