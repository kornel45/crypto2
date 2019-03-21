from common import str2bin, rc4, num2hex


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
    return rc4(key, n, t, ksa_alg)[d:]


if __name__ == '__main__':
    x = rc4_rs_drop_d('Wiki', 16, 16, 0, ksa_rs)
    print(num2hex(x))
