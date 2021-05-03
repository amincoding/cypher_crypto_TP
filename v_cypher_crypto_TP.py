#!usr/bin/python3

"""
    alpha :  Aa$Bb£Cc.Dd?Ee/Ff!Gg,Hh;Ii§Jj%Kk*Ll+Mm-Nn~Oo#Pp{Qq}Rr@Ss^Tt\\Uu`Vv<Ww>Xx¤Yy^Zz=
    author : amin abdedaiem
    date & time : april 5th 2021
    subject :  Vigenere Cipher cryptography 
    link : https://github.com/amincoding/crypted_crypto_TP


"""
import json
import string
from math import sqrt

path_to_json = "secrets.json"

with open(path_to_json, "r") as p:
    info = json.load(p)

Tashfiiiir_alphabits2 = info["alphabits"]
Tashfiiiir_alphabits = string.ascii_uppercase + string.ascii_lowercase + " "
key = info["key"]

text_to_code = dict(zip(Tashfiiiir_alphabits , range(len(Tashfiiiir_alphabits))))
code_to_text = dict(zip(range(len(Tashfiiiir_alphabits)),Tashfiiiir_alphabits))

# creating the function that it does all the encryption then add to it a last step through out a quick function
def Tashfiiiir(text , cle):
    Moshafar = ""
    split_text_cle = [text[i:i + len(cle)] for i in range(0 , len(text) , len(cle))]

    # for split in split_text_cle:
    #     print(split)

    for tag in split_text_cle:
        i = 0
        for alphabet in tag:
            Location = (text_to_code[alphabet] + text_to_code[cle[i]]) % len(Tashfiiiir_alphabits)
            Moshafar += code_to_text[Location]
            i += 1
    
    return Moshafar

def Break_Tashfiiiir(crypted , cle):
    not_Moshafar = ""
    split_cypted_cle = [crypted[i:i + len(cle)] for i in range(0 , len(crypted) , len(cle))]

    for tag in split_cypted_cle:
        i = 0
        for alphabet in tag:
            Location = (text_to_code[alphabet] - text_to_code[cle[i]]) % len(Tashfiiiir_alphabits)
            not_Moshafar += code_to_text[Location]
            i += 1 

    return not_Moshafar

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

    inti_attack(reslt)

# main function
if __name__ == '__main__':
    main()