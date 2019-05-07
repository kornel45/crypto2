from typing import List

_key_128 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut nisi vestibulum, condimentum sem vitae, cursus nisi. Donec non ex'
_key_64 = "En's hard to fail, but it's worse never to have tried to succeed"
_key_40 = "It's hard to fail, but it's worse never to have tried to succeed"[:40]
KEYS = {40: _key_40, 64: _key_64, 128: _key_128}


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def str2num(lst: str or list):
    return [ord(x) for x in lst]


def str2bin(key):
    return ''.join(format(ord(x), '08b') for x in key)


def num2bin(lst):
    return ''.join(format(x, 'b') for x in lst)


def num2hex(lst: List[int]):
    return ''.join([format(x, '02X') for x in lst])


def prga(s: List[int], n: int, d: int):
    i = j = 0
    tmp_d = 0
    while True:
        tmp_d += 1
        i = (i + 1) % n
        j = (j + s[i]) % n
        swap(s, i, j)
        z = s[(s[i] + s[j]) % n]
        if tmp_d > d:
            tmp_d = 0
            yield z


def rc4(key: str, n: int, t: int, d: int, ksa):
    s = ksa(key, n, t)
    return prga(s, n, d)
