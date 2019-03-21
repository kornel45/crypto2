from common import str2num, rc4, num2hex


def ksa_sst(key: str, n: int, t: int):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))

    marked_set = set()
    marked_num = 0
    j = n
    i = 0
    while marked_num < n:
        i = i % n
        j = (j + s[i % n] + num_key[i % key_length]) % n
        s[i], s[j] = s[j], s[i]

        if marked_num < n / 2:
            if s[i] not in marked_set and s[j] not in marked_set:
                marked_set.add(s[i])
                marked_num += 1
        else:
            if (s[i] not in marked_set and s[j] in marked_set) or (s[i] not in marked_set and i == j):
                marked_set.add(s[i])
                marked_num += 1
        i += 1
    return s


def rc4_rs_drop_d(key: str, n: int, t: int, d: int, ksa_alg):
    return rc4(key, n, t, ksa_alg)[d:]


if __name__ == '__main__':
    x = rc4_rs_drop_d('Wiki', 16, 16, 0, ksa_sst)
    print(num2hex(x))
