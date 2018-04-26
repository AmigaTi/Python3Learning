#!/usr/bin/python
# -*- coding: utf-8 -*-


def caesar_cipher_encrypt(d, shift=13):
    e = {}
    for c in (65, 97):
        for i in range(26):
            e[chr(i + c)] = chr((i+26-shift) % 26 + c)
    print(e)
    return "".join([e.get(c, c) for c in d])


def caesar_cipher_decrypt(e, shift=13):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + shift) % 26 + c)
    print(d)
    return "".join([d.get(c, c) for c in e])


s = """Gur Mra bs Clguba, ol Gvz Crgref"""
print(s)                            # Gur Mra bs Clguba, ol Gvz Crgref

de = caesar_cipher_decrypt(s)
print(de)                           # The Zen of Python, by Tim Peters

en = caesar_cipher_encrypt(de)
print(en)                           # Gur Mra bs Clguba, ol Gvz Crgref

de = caesar_cipher_decrypt(en)
print(de)                           # The Zen of Python, by Tim Peters

print('===' * 20)

s = '''Shellever - make it better.'''
en = caesar_cipher_encrypt(s, 10)
print(en)                           # Ixubbuluh - cqau yj rujjuh.

de = caesar_cipher_decrypt(en, 10)
print(de)                           # Shellever - make it better.
