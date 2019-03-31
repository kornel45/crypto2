from common import str2num, rc4, num2hex, swap


def ksa_sst(key: str, n: int, t: int):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))

    marked_lst = [False for _ in range(n)]
    marked_lst[-1] = True
    marked_num = 1
    j = n
    i = 0
    while marked_num < n:
        i = i % n
        j = (j + s[i % n] + num_key[i % key_length]) % n
        swap(s, i, j)
        if marked_num < n / 2:
            if not marked_lst[j] and not marked_lst[i]:
                marked_lst[j] = True
                marked_num += 1
        else:
            if (not marked_lst[j] and marked_lst[i]) or (not marked_lst[j] and i == j):
                marked_lst[j] = True
                marked_num += 1
        swap(marked_lst, i, j)
        i += 1
    return s


if __name__ == '__main__':
    x = rc4('Wiki', 16, 16, 0, ksa_sst)
    print(num2hex(x))
