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

# Defaults
SEQ_LEN = 7
MAX_KEY_LEN = 8
EN_IC = 0.67
EN_REL_FREQ = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015,
               'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
               'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,
               'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}


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

    for tag in split_text_cle:
        i = 0
        for alphabet in tag:
            Location = (text_to_code[alphabet] + text_to_code[cle[i]]) % len(Tashfiiiir_alphabits)
            Moshafar += code_to_text[Location]
            i += 1
    
    return Moshafar
# MIMIMIMIMIMIMIMIMIMIMI 
# creating the function that it does all the decryption then add to it a last step through out a quick function
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

def _decypher(cyphertext, key):
    letters = string.ascii_uppercase
    shifts = [letters.index(letter) for letter in key]
    blocks = processing.get_blocks(text=cyphertext,size=len(key))
    cols = processing.get_columns(blocks)
    decyphered_blocks = processing.to_blocks([fa.shift(col, shift) for col, shift in zip(cols, shifts)])
    decyphered = ''.join(decyphered_blocks)
    return decyphered

def restore_key(cyphertext, key_len):
    key = ''
    blocks = processing.get_blocks(text=cyphertext, size=key_len)
    columns = processing.get_columns(blocks)
    frequencies = _get_letter_frequencies(text=cyphertext)
    for column in columns:
        key += _find_key_letter(text=column, lf=frequencies)
    return key

def _repeated_seq_pos(text, seq_len):
    seq_pos = {}  # entries of sequence : [positions]
    for i, char in enumerate(text):
        next_seq = text[i:i+seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
    repeated = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    rep_seq_pos = [(seq, seq_pos[seq]) for seq in repeated]
    return rep_seq_pos


def _get_spacings(positions):
    return [positions[i+1] - positions[i] for i in range(len(positions)-1)]


def _get_factors(number):
    factors = set()
    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)
    return sorted(factors)


def _candidate_key_lengths(factor_lists, max_key_len):
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]
    # exclude factors larger than suspected max key length
    candidate_lengths = list(filter(lambda x:  x <= max_key_len, all_factors))
    # sort by probability (descending)
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)
    return sorted_candidates


def find_key_length(cyphertext, seq_len, max_key_len):
    # find repeated sequences and their positions
    rsp = _repeated_seq_pos(text=cyphertext, seq_len=seq_len)
    seq_spc = {}
    for seq, positions in rsp:
        seq_spc[seq] = _get_spacings(positions)
    # calculate spacings between positions of each repeated
    # sequence and factor out spacings
    factor_lists = []
    for spacings in seq_spc.values():
        for space in spacings:
            factor_lists.append(_get_factors(number=space))
    # get common factors by descending frequency,
    # which constitute candidate key lengths
    ckl = _candidate_key_lengths(factor_lists=factor_lists, max_key_len=max_key_len)
    key_len = ckl[0]
    return key_len



def inti_attack(file):
        key_len = 0
        print('Applying kasiski examination\n')
        key_len = find_key_length(cyphertext=result, seq_len=SEQ_LEN, max_key_len=MAX_KEY_LEN)
        key = restore_key(result, key_len)
        decyphered = _decypher(result, key)
        print('Chosen key length: '+str(key_len))
        print('Restored key: '+str(key))
        print('Plaintext: '+str(decyphered))

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

    # inti_attack(reslt)

# main function
if __name__ == '__main__':
    main()