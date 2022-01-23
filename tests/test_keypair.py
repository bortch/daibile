import unittest
from key_pair import KeyPair


class TestKeyPair(unittest.TestCase):
    def test_key_pair_creation(self):
        # Create 2 key pairs sharing the same seed
        key = KeyPair()
        key2 = KeyPair(key.seed)
        self.assertEqual(key.seed, key2.seed)
        self.assertEqual(key.private_key, key2.private_key)
        self.assertEqual(key.public_key, key2.public_key)
        # Create a third key pairs which should be different
        key3 = KeyPair()
        self.assertNotEqual(key.seed, key3.seed)
        self.assertNotEqual(key.private_key, key3.private_key)
        self.assertNotEqual(key.public_key, key3.public_key)
