import abc
from record_type import RecordType
import time
import hashlib


class RecordInterface(metaclass=abc.ABCMeta):

    _type: RecordType
    _timestamp: float
    # transaction data
    _data: dict
    # transaction id (hash of the whole transaction data)
    _id: str
    # digital signature
    _digital_signature: str
    # public key
    _pub_key: str

    def __init__(self, type, data) -> None:
        self._type = type
        self._timestamp = time.time()
        self._data = data

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_type') and
                callable(subclass.get_record) and
                hasattr(subclass, 'get_record_size') and
                callable(subclass.get_record_size) or
                NotImplemented)

    def _hash(self):
        """this method is used to hash the record twice. 
        Ferguson and Schneier says it makes SHA-256 invulnerable 
        to 'length-extensio' attack"""
        h = ""
        for key in sorted(self.__dict__.keys()):
            if key == "_id":
                continue
            h += hashlib.sha256(str(self.__dict__[key]).encode()).hexdigest()
        return hashlib.sha256(h.encode()).hexdigest()

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

    @property
    def timestamp(self) -> float:
        """Return the timestamp of the record"""
        return self._timestamp

    @property
    def id(self) -> str:
        """Return the id of the record"""
        return self._id

    @id.setter
    def id(self, value: dict):
        _id = ""
        for key, val in value.items():
            _id += hashlib.sha256(val).hexdigest()
        self._id = hashlib.sha256(_id.encode()).hexdigest()
