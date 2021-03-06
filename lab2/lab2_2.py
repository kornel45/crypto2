import sys

from common import str2bin, rc4, num2hex, num2bin


def ksa_rs(key: str, n: int, t: int):
    s = list(range(n))
    bit_key = str2bin(key)
    l = len(bit_key)
    for r in range(t):
        top = []
        bot = []
        for i in range(n):
            if bit_key[(r * n + i) % l] == '0':
                top.append(s[i])
            else:
                bot.append(s[i])
        top.extend(bot)
        s = top.copy()
    return s


def rc4_rs_drop_d(key: str, n: int, t: int, d: int, ksa_alg):
    return rc4(key, n, t, d, ksa_alg)


if __name__ == '__main__':
    stream = rc4('Wiki', 16, 16, 0, ksa_rs)

    for _ in range(10 ** 1):
        sys.stdout.buffer.write(bytes([next(stream)]))
