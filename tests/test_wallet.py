import unittest
from wallet import Wallet
from key_pair import KeyPair
from transaction import Transaction, TransactionInput, TransactionOutput
from ecdsa import VerifyingKey, SECP256k1
from crypt_utils import hash_object
from hashlib import sha256
from ecdsa.util import sigencode_string, sigdecode_string, sigencode_der


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
        satoshi_public_key = satoshi_wallet.key_chain["satoshi"].public_key.to_string(
        )
        satoshi_public_address = satoshi_wallet.public_address("satoshi")

        bortch_wallet = Wallet()
        bortch_key_pair = KeyPair(name="bortch")
        bortch_wallet.add_key_pair(bortch_key_pair)

        input = TransactionInput("previous_transaction_id", 0)
        output = TransactionOutput(100, bortch_wallet.public_address("bortch"))
        transaction = satoshi_wallet.create_transaction(
            [output], [input], key_chain_name="satoshi")
        print(transaction.to_string())

        node_verifying_key = VerifyingKey.from_string(
            satoshi_public_key, curve=SECP256k1)
        input_to_verify = TransactionInput("previous_transaction_id", 0)
        input_to_verify.digital_signature = satoshi_public_address
        input_to_verify.full_public_key = satoshi_public_key
        hash_to_verify = hash_object(input_to_verify)
        self.assertTrue(node_verifying_key.verify_digest(
            input.digital_signature, hash_to_verify, sigdecode=sigdecode_string))
