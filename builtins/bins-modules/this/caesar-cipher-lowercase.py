#!/usr/bin/python
# -*- coding: utf-8 -*-

import string


'''
凯撒密码属于替换密码的一种，替换密码就是指用一个别的字母来替换当前的字母。
比如我和对方约定一个替换表： l -> h，o -> a，v -> t，然后我发送love给对方，对方按照对照表就知道我发送的其实是hate。
凯撒密码使用的是将正常的 26 个英文字母进行移位替换，通常设定 shift 值为 3，相当于 a -> d，b -> e，c -> f...
'''


lowercase = string.ascii_lowercase


def substitution(text, key_table):
    text = text.lower()
    result = ''
    for l in text:
        i = lowercase.find(l)
        if i < 0:
            result += l
        else:
            result += key_table[i]
    return result


def caesar_cipher_encrypt(text, shift):
    key_table = lowercase[shift:] + lowercase[:shift]
    return substitution(text, key_table)


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# 破解，遍历26个不同的shift值，查看哪个是有意义的
def caesar_cipher_crack(text):
    for i in range(26):
        key_table = lowercase[-i:] + lowercase[:-i]
        print(substitution(text, key_table)[:12], '| shift is ', i)


init_text = '''
We intend to begin on the first of February unrestricted submarine warfare.
We shall endeavor in spite of this to keep the United States of America neutral.
In the event of this not succeeding, we make Mexico a proposal of alliance on
the following basis: make war together, make peace together, generous financial
support and an understanding on our part that Mexico is to reconquer the lost territory
in Texas, New Mexico, and Arizona. The settlement in detail is left to you. You will
inform the President of the above most secretly as soon as the outbreak of war with the
United States of America is certain and add the suggestion that he should, on his own initiative,
invite Japan to immediate adherence and at the same time mediate between Japan and ourselves.
Please call the President's attention to the fact that the ruthless employment of our submarines
now offers the prospect of compelling England in a few months to make peace.
'''

cipher_text_encrypt = caesar_cipher_encrypt(init_text, 13)
print(cipher_text_encrypt)

cipher_text_decrypt = caesar_cipher_decrypt(cipher_text_encrypt, 13)
print(cipher_text_decrypt)
