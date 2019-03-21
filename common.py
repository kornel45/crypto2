from typing import List

key_5 = 'korne'
key_40 = 'encryption scheme uses two algorithmspzd'
key_64 = 'PBKDF2 password strengthener; and the CCM and OCB authenticated-'
key_128 = "Main reason not to use SJCL (and yes, it will sound stupid from a crypto perspective) is " \
          "that I don't want to load it on every p"
N = [16, 64, 256]
KEYS = [key_40, key_64, key_128]
D = [0, 1, 2, 3]


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def str2num(lst: str or list):
    return [ord(x) for x in lst]


def str2bin(key):
    return ''.join(format(ord(x), '08b') for x in key)


def num2bin(lst):
    return ''.join(format(x, '08b') for x in lst)


def num2hex(lst: List[int]):
    return ''.join([format(x, '02X') for x in lst])


def prga(s: List[int], n: int):
    i = j = 0
    while True:
        i = (i + 1) % n
        j = (j + s[i]) % n
        swap(s, i, j)
        z = s[(s[i] + s[j]) % n]
        yield z


def rc4(key: str, n: int, t: int, ksa):
    s = ksa(key, n, t)
    stream = prga(s, n)
    return [next(stream) for _ in range(len(s))]
