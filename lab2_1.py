from common import str2num, rc4, num2hex


def ksa(key: str, n: int, t: int):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))
    j = 0
    for i in range(t):
        j = (j + s[i % n] + num_key[i % key_length]) % n
        s[i % n], s[j] = s[j], s[i % n]
    return s


def rc4_drop_d(key: str, n: int, t: int, d: int, ksa_alg):
    return rc4(key, n, t, ksa_alg)[d:]


if __name__ == '__main__':
    x = rc4_drop_d('Wiki', 256, 256, 0, ksa)
    print(num2hex(x))
