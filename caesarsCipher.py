import random
from random import randint


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

plaintext = input("Message to encrypt: ")

#   This splits the individual letters from the input
plaintext_sep = list(plaintext.strip())

def encrypt():
    
    
    plaintext_encrypted = []
    
#   Iterates the length of user input
    for i in range(len(plaintext_sep)):
        if plaintext_sep[i] in alphabet:
            rot = alphabet.index(plaintext_sep[i])
            try:

                #FIXME:
                # When 'R' = 'Z', it does not work
                
                rot = rot + 13
                if(rot > int(len(alphabet))):
                    
                    rot = rot - int(len(alphabet)) 
#                    print(rot)
#                    print(alphabet[rot])
                    plaintext_encrypted.append(alphabet[rot])
                else:
                    #print(rot)
#                    print(alphabet[rot])
                    plaintext_encrypted.append(alphabet[rot])

            except IndexError:
                print("Rot going too far in list")
                print(rot)
            

        else:
            pass
        

    pt_encryp_string = ''.join(plaintext_encrypted)
#    print(pt_encryp_string)
    
    return pt_encryp_string, rot
    
    



def decrypt():
    decrypt_string = encrypt()
    rot = decrypt_string[1]
    

    print(decrypt_string[0])
    print(rot)

#encrypt()

decrypt()