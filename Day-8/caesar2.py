def rotate(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    higher_alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z"]
    cipher_text = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            key = key % 26
            ind = alphabet.index(text[i])
            cipher_text += alphabet[ind + key]
            
        if text[i] in higher_alpha:
            key = key % 26
            ind = higher_alpha.index(text[i])
            cipher_text += higher_alpha[ind + key]
            
        elif text[i] == " ":
            cipher_text += " "
        
        elif text[i] not in alphabet and higher_alpha:
            cipher_text += text[i]

        
    return cipher_text
