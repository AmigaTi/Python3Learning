#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64

bs = base64.b64encode(b'binary\x00string')
print(bs)            # b'YmluYXJ5AHN0cmluZw=='

bs = base64.b64decode(bs)
print(bs)            # b'binary\x00string'

bs = base64.b64encode(b'abcde')
print(bs)            # b'YWJjZGU='

bs = base64.b64encode(b'phreq')
print(bs)            # b'cGhyZXE='

bs = base64.b64encode(b'hyperfor')
print(bs)            # b'aHlwZXJmb3I='

bs = base64.b64encode(b'icentury')
print(bs)            # b'aWNlbnR1cnk='

bs = base64.b64encode(b'shellever')
print(bs)            # b'c2hlbGxldmVy'
print('---------------------------')


# 由于标准的Base64编码后可能出现字符+和/，
# 在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，
# 其实就是把字符+和/分别变成-和_
bs = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bs)       # b'abcd++//'

bs = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bs)       # b'abcd--__'

bs = base64.urlsafe_b64decode('abcd--__')
print(bs)       # b'i\xb7\x1d\xfb\xef\xff'
print('---------------------------')


# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面
# 会造成歧义，所以很多Base64编码后会把=去掉

# 因为Base64是把3个字节变为4个字节，所以Base64编码的长度为4的倍数，
# 因此加上=把Base64字符串的长度变为4的倍数，就可以正常解码。

# 标准Base64
# 'abcd' -> 'YWJjZA=='
# 自动去掉=
# 'abcd' -> 'YWJjZA'


# 能处理去掉=的base64解码函数
# bytes
def safe_base64_decode(s):
    str_ascii = s.decode('ascii')
    r = len(str_ascii) % 4
    if r == 0:
        str_bytes = str_ascii.encode('ascii')
        return base64.b64decode(str_bytes)
    else:
        r = 4 - r
        while r:
            str_ascii += '='
            r -= 1
        str_bytes = str_ascii.encode('ascii')
        print('automatically modified: %s => %s' % (s, str_bytes))
        return base64.b64decode(str_bytes)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
assert b'abcde' == safe_base64_decode(b'YWJjZGU='), safe_base64_decode('YWJjZGU=')
assert b'abcde' == safe_base64_decode(b'YWJjZGU'), safe_base64_decode('YWJjZGU')
print('Pass')
'''
automatically modified: b'YWJjZA' => b'YWJjZA=='
automatically modified: b'YWJjZGU' => b'YWJjZGU='
Pass
'''


# bytes & str
def safe_base64_decode2(s):
    return base64.b64decode(s + b'=' * (4 - len(s) % 4))


print('start safe_base64_decode2...')
assert b'abcd' == safe_base64_decode2(b'YWJjZA=='), safe_base64_decode2('YWJjZA==')
assert b'abcd' == safe_base64_decode2(b'YWJjZA'), safe_base64_decode2('YWJjZA')
assert b'abcde' == safe_base64_decode2(b'YWJjZGU='), safe_base64_decode2('YWJjZGU=')
assert b'abcde' == safe_base64_decode2(b'YWJjZGU'), safe_base64_decode2('YWJjZGU')
print('end safe_base64_decode2.')
'''
start safe_base64_decode2...
end safe_base64_decode2.
'''