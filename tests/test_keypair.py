import unittest
from key_pair import KeyPair
import os


class TestKeyPair(unittest.TestCase):

    path = os.getcwd() + "/tests/"

    def test_key_pair_creation(self):
        # Create 2 key pairs sharing the same seed
        key = KeyPair(name="satoshi_1", path=self.path)
        key2 = KeyPair(name="satoshi_2", seed=key.seed, path=self.path)
        self.assertEqual(key.seed, key2.seed)
        self.assertEqual(key.private_key_hex, key2.private_key_hex)
        self.assertEqual(key.public_key_hex, key2.public_key_hex)
        # Create a third key pairs which should be different
        key3 = KeyPair(name="bortch", path=self.path)
        self.assertNotEqual(key.seed, key3.seed)
        self.assertNotEqual(key.private_key_hex, key3.private_key_hex)
        self.assertNotEqual(key.public_key_hex, key3.public_key_hex)
