import random

from math import gcd


def gen_coprime(q):
    r = q
    while gcd(q, r) != 1:
        r = random.randint(2, q)
    return r


def mod_inv(r, q):
    g, t, _ = egcd(r, q)
    if g == 1:
        return t % q


def egcd(a, b):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while b != 0:
        z, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - z * x1
        y0, y1 = y1, y0 - z * y1
    return a, x0, y0


def gen_superincreasing_sequence(n, next_int_range):
    w = []
    total = 0
    for i in range(n):
        new_rand = random.randint(total + 1, 2 * total + next_int_range)
        total += new_rand
        w.append(new_rand)
    return w, total


class MerkleHellman:
    next_int_range = 100

    def __init__(self, m):
        self.m = m
        self.n = len(m)

    def gen_key(self):
        w, total = gen_superincreasing_sequence(self.n, MerkleHellman.next_int_range)
        q = random.randint(total + 1, 2 * total + MerkleHellman.next_int_range)
        r = gen_coprime(q)
        public_key = [r * w % q for w in w]
        private_key = [w, q, r]
        return public_key, private_key

    def encrypt(self, public_key):
        return sum([m * k for m, k in zip(self.m, public_key)])

    def decrypt(self, cipher, private_key):
        w, q, r = private_key
        s = mod_inv(r, q)
        c_prim = cipher * s % q
        decrypted = [-1 for _ in range(self.n)]
        for i in range(self.n - 1, -1, -1):
            to_subtract = int(w[i] <= c_prim)
            decrypted[i - self.n] = to_subtract
            c_prim -= w[i] * to_subtract
        return decrypted


if __name__ == '__main__':
    msg = [random.randint(0, 1) for _ in range(random.randint(0, 10))]
    m = MerkleHellman(msg)
    pub_key, priv_key = m.gen_key()
    encrypted = m.encrypt(pub_key)
    decrypted = m.decrypt(encrypted, priv_key)
    assert msg == decrypted
