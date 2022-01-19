import abc
from dataclasses import dataclass
from record_type import RecordType
import time
import hashlib
import json


class RecordInterface(metaclass=abc.ABCMeta):

    _type: RecordType
    _timestamp: float
    _hash: str
    _data: dict

    def __init__(self, type, data) -> None:
        self._type = type
        self._timestamp = time.time()
        self._data = data
        self._hash = ""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_type') and
                callable(subclass.get_record) and
                hasattr(subclass, 'get_record_size') and
                callable(subclass.get_record_size) or
                NotImplemented)

    @classmethod
    def _hash_record(cls, data: dict):
        sorted_data = json.dumps(data, sort_keys=True)
        return hashlib.sha256(sorted_data.encode()).hexdigest()

    @property
    @abc.abstractmethod
    def type(self) -> RecordType:
        """Return the type of the record"""
        raise NotImplementedError

    @property
    def data(self) -> dict:
        """Return the data of the record"""
        return self._data

    @data.setter
    def data(self, value: dict):
        self._data = value
        self._hash = self._hash_record(self._data)

    @property
    def timestamp(self) -> float:
        """Return the timestamp of the record"""
        return self._timestamp

    @property
    def hash(self) -> str:
        """Return the hash of the record"""
        return self._hash
