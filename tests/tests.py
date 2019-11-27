# -*- coding: utf-8 -*-
# vim: sts=2:ts=2:sw=2
import random
import string
from unittest import TestCase, main

import til_shorty

class Test(TestCase):

    def test_shorty_numbers_google_datastore_like(self):
        for i in range(1000):
            rand = random.randrange(1000000000000000, 9999999999999999)
            short = til_shorty.short(rand)
            self.assertEqual(rand, til_shorty.expand(short))

    def test_shorty_numbers(self):
        for i in range(1000):
            short = til_shorty.short(i)
            self.assertEqual(i, til_shorty.expand(short))

    def test_shorty_alphabet_numbers(self):
        for i in range(1000):
            short = til_shorty.short(i, alphabet=string.digits)
            self.assertEqual(str(i), short)

    def test_shorty_alphabet(self):
        for i in range(len(til_shorty.DEFAULT_ALPHABET)):
            short = til_shorty.short(i, til_shorty.DEFAULT_ALPHABET)
            self.assertEqual(til_shorty.DEFAULT_ALPHABET[i], short)


if __name__ == '__main__':
    main()