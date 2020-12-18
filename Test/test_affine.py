#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Affine
from secretpy import alphabets
import unittest


class TestAffine(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
   
    )

    key = ([5, 8], [5, 8], [7, 8], [5, 8], [5, 8])

    plaintext = (
        u"affinecipher")

    ciphertext = (
        u"ihhwvcswfrcp")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Affine().encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Affine().decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
