import unittest
from wallet import Wallet
from key_pair import KeyPair
from transaction import Transaction, TransactionInput, TransactionOutput


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
        bortch_key_pair = KeyPair(name="bortch")
        bortch_wallet.add_key_pair(bortch_key_pair)

        input = TransactionInput("previous_transaction_id", 0)
        output = TransactionOutput(100, bortch_key_pair.public_key_hex)
        transaction = satoshi_wallet.create_transaction(
            [output], [input], key_chain_name="satoshi")
        print(transaction.to_string())
