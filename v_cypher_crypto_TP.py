#!usr/bin/python3

"""
	alpha :  
	author : amin abdedaiem
	date & time : april 5th 2021
	subject :  Vigenere Cipher cryptography 
	link : https://github.com/amincoding/crypted_crypto_TP


"""
import json
import string
from math import sqrt
import re
import string
import math
import itertools
from collections import defaultdict, Counter
from operator import itemgetter
import sys

ALPHABET = string.ascii_lowercase
def _assert_alphabet(text):
    assert all(c in ALPHABET for c in text)

def alphabet_diff(a, b):
    return ALPHABET[(ALPHABET.index(a) - ALPHABET.index(b)) % len(ALPHABET)]

def alphabet_sum(a, b):
    return ALPHABET[(ALPHABET.index(a) + ALPHABET.index(b)) % len(ALPHABET)]

def text2message(text):
    return "".join(c for c in text.lower() if c in ALPHABET)

def print_enumerated(iterable, s):
    print(f'[*] {s}:')
    for i, item in enumerate(iterable, start=1):
        t = str(item)
        if len(t) > 100:
            print(f'{i: >2}: {t[:80]}...')
        else:
            print(f'{i: >2}: {t}')

def _vigener_encrypt(message, key):
    
    _assert_alphabet(message)
    _assert_alphabet(key)
    
    key_len = len(key)
    ciphertext = ''
    
    for i, mi in enumerate(message):
        ki = key[i % key_len]
        ci = alphabet_sum(mi, ki)
        ciphertext += ci
    
    return ciphertext

def vigener_encrypt(text, key,preserve_whitespace=False):
    if preserve_whitespace:
        wss = [m.start() for m in re.finditer(' ', text)]
        ciphertext = vigener_encrypt(text.replace(' ', ''), key)
        l = list(ciphertext)
        for p in wss:
            l.insert(p, ' ')
        return ''.join(l)
    else:
        return _vigener_encrypt(text2message(text), key.lower())

def kasiski_examination(ciphertext, seq_len, max_key_len, *, verbose=False):
    
    _assert_alphabet(ciphertext)

    seq_positions = defaultdict(list)  # {seq: [pos]}
    for i in range(len(ciphertext) - seq_len):
        seq_positions[ciphertext[i : i + seq_len]].append(i)
    
    seq_positions = {
        seq: positions
        for seq, positions in seq_positions.items()
        if len(positions) >= 2
    }
    assert len(seq_positions) > 0, f"No repeated sequences of length {seq_len}"
    
    if verbose:
        print("[*] Positions:")
        for seq, positions in seq_positions.items():
            print(f"    {seq}: {positions}")

    seq_spacings = defaultdict(list)  # {seq: [space]}
    for seq, positions in seq_positions.items():
        for a, b in zip(positions, positions[1:]):
            seq_spacings[seq].append(b - a)
    
    if verbose:
        print("[*] Spacings:")
        for seq, spacings in seq_spacings.items():
            print(f"    {seq}: {spacings}")
    
    # Count factors (<=max_key_len) of all spacings
    factor_count = Counter()
    for spacings in seq_spacings.values():
        for space in spacings:
            for f in range(2, min(max_key_len, int(math.sqrt(space)) + 1)):
                if f != 2:
                    if space % f == 0:
                        factor_count[f] += 1
    
    if verbose:
        print("[*] Factor counts:")
        for f, count in factor_count.items():
            print(f"    {f}: {count}")
    
    key_len = factor_count.most_common()[0][0] 
    
    if verbose:
        print(f"[+] The most probable key length: {key_len}")
    
    return key_len

def _freq(text):
    return Counter(text)

def _blocks(ciphertext, key_len):
    return [''.join(ciphertext[shift + i]
                    for i in range(0, len(ciphertext) - shift, key_len))
            for shift in range(key_len)]

def frequency_analysis(ciphertext, key_len, text_freq, *, verbose=False):
    _assert_alphabet(ciphertext)
    
    blocks = _blocks(ciphertext, key_len)
    block_freqs = [_freq(block) for block in blocks]
    most_common_letter = text_freq.most_common()[0][0]
    
    if verbose:
        print_enumerated(blocks, 'Blocks')
        print("[*] Block frequencies (most common):")
        for i, block_freq in enumerate(block_freqs, start=1):
            print(f"{i: >2}: {block_freq.most_common(7)}")
        print(f"[*] Most common letter in original text: '{most_common_letter}'")
    
    # Find the most probable key
    key = ''
    for i, block in enumerate(blocks):
        # Note: mi + ki = ci, then ki = ci - mi
        ci = block_freqs[i].most_common()[0][0]
        ki = alphabet_diff(ci, most_common_letter)
        key += ki
    
    if verbose:
        print(f"[+] Most probable key: '{key}'")
    
    return key

def vigener_decrypt(ciphertext, key):
    
    key_len = len(key)
    message = ''
    
    for i, ci in enumerate(ciphertext):
        ki = key[i % key_len]
        mi = alphabet_diff(ci, ki)
        message += mi
    
    return message

def callEncrypt(message):
	text = message[0]
	key = message[1]
	res = vigener_encrypt(text, key,preserve_whitespace=False)
	return res

def callDecrypt(message):
    text = message[0]
    key = message[1]
    res = vigener_decrypt(text, key)
    return res

def callKasisiki(message):
    text = message[0]
    res = kasiski_examination(text, 4, 12, verbose=False)
    return res 

def callKey(keyLengh):
	key = keyLengh
	

