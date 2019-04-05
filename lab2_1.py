from common import str2num, rc4
from signal import signal, SIGPIPE, SIG_DFL
import sys

signal(SIGPIPE, SIG_DFL)


def ksa(key: str, n: int, t: int):
    num_key = str2num(key)
    key_length = len(num_key)
    s = list(range(n))
    j = 0
    for i in range(t):
        j = (j + s[i % n] + num_key[i % key_length]) % n
        s[i % n], s[j] = s[j], s[i % n]
    return s


if __name__ == '__main__':
    key = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut nisi vestibulum, condimentum sem vitae, cursus nisi. Donec non ex'
    stream = rc4(key, 16, 16, 0, ksa)
    for i in range(10 ** 1):
        sys.stdout.buffer.write(bytes([next(stream)]))
