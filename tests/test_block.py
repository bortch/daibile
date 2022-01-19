import unittest
import time

from block import Block
from transaction import Transaction


class TestBlock(unittest.TestCase):

    def test_block_creation(self):
        now = time.time()
        previous_hash = "previous_hash"
        block = Block(index=1, timestamp=now, previous_hash=previous_hash)
        self.assertEqual(block.index, 1)
        self.assertEqual(block.timestamp, now)
        self.assertEqual(block.previous_hash, previous_hash)
        self.assertEqual(block.proof, None)
        self.assertEqual(block.records, [])

    def test_add_record(self):
        now = time.time()
        previous_hash = "previous_hash"
        block = Block(index=1, timestamp=now, previous_hash=previous_hash)
        record = Transaction(sender="sender", recipient="recipient", amount=10)
        block.add_record(record)
        self.assertEqual(block.records, [record])


if __name__ == '__main__':
    unittest.main()
