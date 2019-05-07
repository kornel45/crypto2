from common import rc4, KEYS, num2hex
from lab2_1 import ksa
from lab2_2 import ksa_rs
from lab2_3 import ksa_sst
from signal import signal, SIGPIPE, SIG_DFL
import math
import itertools
import os


signal(SIGPIPE, SIG_DFL)


def gen_numbers(file_name, n_numbers, key, n, t, d, ksa):
    with open(file_name, 'w') as f:
        stream = rc4(KEYS[key], n, t, d, ksa)
        for i in range(10 ** n_numbers):
            val = num2hex([next(stream)])
            f.write(val + '\n')


if __name__ == '__main__':
    N = [256]
    KEY_LENGTH = [40]
    D = [0]
    dir_path = 'results/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        for file in os.listdir(dir_path):
            if '.' in file:
                os.remove(os.path.join(dir_path, file))
    for n, key, d in itertools.product(N, KEY_LENGTH, D):
        rc4_d_file = '{dir}rc4_d{d}_key{key}_n{n}.txt'.format(dir=dir_path, n=n, key=key, d=d)
        rc4_rs_d_file = '{dir}rc4_rs_d{d}_key{key}_n{n}.txt'.format(dir=dir_path, n=n, key=key, d=d)
        rc4_sst_file = '{dir}rc4_sst{d}_key{key}_n{n}.txt'.format(dir=dir_path, n=n, key=key, d=d)
        gen_numbers(rc4_d_file, 7, key, n, n, d, ksa)
        gen_numbers(rc4_rs_d_file, 7, key, n, int(2 * n * math.log(n)), d, ksa_rs)
        gen_numbers(rc4_sst_file, 7, key, n, n, d, ksa_sst)

