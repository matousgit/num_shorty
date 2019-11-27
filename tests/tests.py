# -*- coding: utf-8 -*-
# vim: sts=2:ts=2:sw=2
import random
import string
from unittest import TestCase, main

import num_shorty

class Test(TestCase):

    def test_shorty_numbers_google_datastore_like(self):
        for i in range(1000):
            rand = random.randrange(1000000000000000, 9999999999999999)
            short = num_shorty.short(rand)
            self.assertEqual(rand, num_shorty.expand(short))

    def test_shorty_numbers(self):
        for i in range(1000):
            short = num_shorty.short(i)
            self.assertEqual(i, num_shorty.expand(short))

    def test_shorty_alphabet_numbers(self):
        for i in range(1000):
            short = num_shorty.short(i, alphabet=string.digits)
            self.assertEqual(str(i), short)

    def test_shorty_alphabet(self):
        for i in range(len(num_shorty.DEFAULT_ALPHABET)):
            short = num_shorty.short(i, num_shorty.DEFAULT_ALPHABET)
            self.assertEqual(num_shorty.DEFAULT_ALPHABET[i], short)


if __name__ == '__main__':
    main()
