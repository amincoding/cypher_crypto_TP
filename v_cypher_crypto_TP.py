#!usr/bin/python3

"""

    author : amin abdedaiem
    date & time : april 5th 2021
    subject :  Vigenere Cipher cryptography 
    link : https://github.com/amincoding/cypher_crypto_TP


"""
import json


path_to_json = "secret.json"

with open(path_to_json, "r") as p:
    info = json.load(p)

Tashfiiiir_alphabits = info["alphabits"]
key = info["key"]

# creating the function that it does all the encryption then add to it a last step through out a quick function
def Tashfiiiir(text , cle):
    pass

# creating the function that it does all the decryption then add to it a last step through out a quick function
def Break_Tashfiiiir(cypher , cle):
    pass

# main execution function
def main():
    
    message = input("enter the message that u want to encrypt : ")
    Tashfiiiir(message ,key)

# main function
if __name__ == '__main__':
    main()