import hashlib
import json


from record_interface import RecordInterface


class Block(object):
    """
    A class to create a block
    """

    def __init__(self, index: int, timestamp: float, previous_hash: str):
        self._index = index
        self._timestamp = timestamp
        self._previous_hash = previous_hash
        self._hash = self.hash_block()
        self._proof = None
        self._records: list[RecordInterface] = []

    def hash_block(self):
        """
        Creates a SHA-256 hash of a Block
        :return: <str>
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_record(self, record):
        """
        Add a record to the block
        :param record: <dict>
        :return: <bool>
        """
        self.records.append(record)
        return True

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def previous_hash(self):
        return self._previous_hash

    @previous_hash.setter
    def previous_hash(self, value):
        self._previous_hash = value

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, value):
        self._hash = value

    @property
    def proof(self):
        return self._proof

    @proof.setter
    def proof(self, value):
        self._proof = value

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        self._records = value

    def to_dict(self):
        """
        Convert a Block object to a dictionary
        :return: <dict>
        """
        return self.__dict__

    def to_json(self):
        """
        Convert a Block object to a JSON string
        :return: <str>
        """
        return json.dumps(self.to_dict())
