import unittest
from wallet import Wallet
from key_pair import KeyPair


class TestWallet(unittest.TestCase):

    def test_create_wallet(self):
        wallet = Wallet()
        self.assertEqual(len(wallet.key_chain), 1)
        self.assertEqual(wallet.key_chain["default"].name, "default")

        # add a new key pair
        wallet.add_key_pair(KeyPair(name="satoshi"))
        self.assertEqual(len(wallet.key_chain), 2)
        self.assertEqual(wallet.key_chain["satoshi"].name, "satoshi")

        # add new default key pair
        wallet.add_key_pair(KeyPair("default"))
        self.assertEqual(len(wallet.key_chain), 3)
        index = len(wallet.key_chain)-1
        self.assertEqual(
            wallet.key_chain[f"default_{index}"].name, f"default_{index}")

    def test_wallet_create_transaction(self):
        satoshi_wallet = Wallet()
        satoshi_wallet.add_key_pair(KeyPair(name="satoshi"))

        bortch_wallet = Wallet()
        bortch_wallet.add_key_pair(KeyPair(name="bortch"))
