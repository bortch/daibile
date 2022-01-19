import time
from block import Block
from record_interface import RecordInterface
from typing import Type


class Blockchain(object):
    """
    This class is responsible to manage the chain of blocks
    """

    def __init__(self) -> None:
        self._chain = []
        # Create the genesis block
        block = Block(index=0,
                      timestamp=time.time(),
                      previous_hash="GENESIS")
        self.current_block = block
        self.chain.append(block)

    def new_block(self, previous_hash=None) -> Block:
        # create a new block and add it to the chain
        block = Block(index=self.last_mined_block.index + 1,
                      timestamp=time.time(), previous_hash=previous_hash)
        self.current_block = block
        return block

    @property
    def chain(self):
        return self._chain

    @property
    def last_mined_block(self) -> Block:
        return self.chain[-1]

    @property
    def current_block(self) -> Block:
        return self._current_block

    @current_block.setter
    def current_block(self, value: Block):
        self._current_block = value

    def add_record(self, record: RecordInterface) -> None:
        """
        Add a record to the block
        :param record: <dict>
        :return: <bool>
        """
        self.current_block.add_record(record)

    def length(self):
        return len(self.chain)
