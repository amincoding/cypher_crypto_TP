#!usr/bin/python3

"""

    author : amin abdedaiem
    date & time : april 5th 2021
    subject :  Vigenere Cipher cryptography 
    link : https://github.com/amincoding/cypher_crypto_TP


"""
import json


path_to_json = "secrets.json"

with open(path_to_json, "r") as p:
    info = json.load(p)

Tashfiiiir_alphabits = info["alphabits"]
key = info["key"]

text_to_code = dict(zip(Tashfiiiir_alphabits , range(len(Tashfiiiir_alphabits))))
code_to_text = dict(zip(range(len(Tashfiiiir_alphabits)),Tashfiiiir_alphabits))

# creating the function that it does all the encryption then add to it a last step through out a quick function
def Tashfiiiir(text , cle):
    Moshafar = ""
    tagging_the_message = [text[i:i + len(cle)] for i in range(0 , len(text) , len(cle))]

    for tag in tagging_the_message:
        i = 0
        for alphabet in tag:
            number = (text_to_code[alphabet] + text_to_code[cle[i]]) % len(text)
            Moshafar += code_to_text[number]
            i += 1
    
    return Moshafar

# creating the function that it does all the decryption then add to it a last step through out a quick function
def Break_Tashfiiiir(cypher , cle):
    not_Moshafar = ""
    tagging_the_message = [cypher[i:i + len(cle)] for i in range(0 , len(cypher) , len(cle))]

    for tag in tagging_the_message:
        i = 0
        for alphabet in tag:
            number = (text_to_code[alphabet] + text_to_code[cle[i]]) % len(cypher)
            not_Moshafar += code_to_text[number]
            i += 1 

    return not_Moshafar

def regex_to_code_spaces():
    pass

# main execution function
def main():
    print("(e)ncrypting or (d)icrypting :")
    test = input("[e][d] : \n")
    if test == "e":
        message = input("enter the message that u want to encrypt : ")
        reslt = Tashfiiiir(message ,key)
        print(reslt)
    elif test == "d":
        message = input("enter the message that u want to decrypt : ")
        reslt = Break_Tashfiiiir(message ,key)
        print(reslt)

# main function
if __name__ == '__main__':
    main()