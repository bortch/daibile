import unittest
from blockchain import Blockchain
from block import Block
import time


class TestBlockchain(unittest.TestCase):

    _blockchain: Blockchain

    def test_blockchain_creation(self):
        blockchain = Blockchain()
        self.assertEqual(blockchain.length(), 1)

    def test_blockchain_add_block(self):
        self._blockchain = Blockchain()
        a_random_block = Block(
            index=0, timestamp=time.time(), previous_hash="GENESIS")
        self.assertEqual(self._blockchain.length(), 1)
        self.assertNotEqual(self._blockchain.current_block.hash,
                            a_random_block.hash)

    def test_blockchain_get_last_block(self):
        pass

    def test_blockchain_get_last_block_index(self):
        pass

    def test_blockchain_get_last_block_hash(self):
        pass

    def test_blockchain_get_last_block_timestamp(self):
        pass

    def test_blockchain_get_last_block_previous_hash(self):
        pass

    def test_blockchain_get_last_block_proof(self):
        pass

    def test_blockchain_get_last_block_records(self):
        pass

    def test_blockchain_get_last_block_record(self):
        pass

    def test_blockchain_get_last_block_record_by_index(self):
        pass

    def test_blockchain_get_last_block_record_by_hash(self):
        pass

    def test_blockchain_get_last_block_record_by_type(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_index(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_hash(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_timestamp(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_previous_hash(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_proof(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_sender(self):
        pass

    def test_blockchain_get_last_block_record_by_type_and_recipient(self):
        pass


if __name__ == '__main__':
    unittest.main()
