import unittest
import time

from blockchain import Blockchain
from block import Block
from transaction import Transaction, TransactionInput, TransactionOutput


class TestBlockchain(unittest.TestCase):

    _blockchain: Blockchain

    def test_blockchain_creation(self):
        """create an instance of blockchain with a genesis block"""
        blockchain = Blockchain()
        self.assertEqual(blockchain.length(), 1)

    def test_blockchain_add_block(self):
        """"""
        self._blockchain = Blockchain()
        added_block = self._blockchain.new_block(previous_hash="GENESIS")
        self.assertNotEqual(added_block, None)

    def test_blockchain_current_block(self):
        self.test_blockchain_add_block()
        self.assertEqual(self._blockchain.current_block.index, 1)

    def test_blockchain_add_record(self):
        self.test_blockchain_add_block()
        inputs = [TransactionInput(
            transaction_id="previous_transaction_hash", output_index=0)]
        outputs = [TransactionOutput(value=10, src_pub_key="my_public_key")]
        record = Transaction(inputs, outputs)
        self._blockchain.add_record(record)
        self.assertEqual(len(self._blockchain.current_block.records), 1)


if __name__ == '__main__':
    unittest.main()
