from dataclasses import dataclass
from enum import Enum
import hashlib
import base58
import ecdsa
from crypt_utils import checksum, is_checksum_valid, add_checksum
from crypt_utils import sha256d, hash160
from record_interface import RecordInterface
from record_type import RecordType


@dataclass
class ScriptSig():
    """
    A class to store the scriptSig of a transaction
    """
    _pub_key: str
    _digital_signature: str


@dataclass
class TransactionInput():
    def __init__(self, transaction_id: str, output_index: int):
        # transaction id to use as source of funds
        self.transaction_id = transaction_id
        # index of the output to use from the transaction
        self.output_index = output_index
        # original public key used for the lock in the output
        self.pub_key = None
        # digital signature to be checked by nodes against the public key
        # ~ScriptSig
        self.digital_signature = None


class TransactionOutput():
    def __init__(self, value: int, src_pub_key: str):
        # value to spend
        self.value = value
        # lock to be unlocked for spending
        # ~scriptPubKey
        self.src_pub_key = hash160(src_pub_key)


class TransactionData():
    def __init__(self, inputs: list[TransactionInput], outputs: list[TransactionOutput]):
        self.inputs = inputs
        self.outputs = outputs


class Transaction(RecordInterface):

    # type of record
    _type: RecordType = RecordType.TRANSACTION
    # data of a transaction
    _data: dict = {"input_addr": [],  # list of input addresses
                   "output_addr": [],
                   "value": 0,
                   "precision": 4,
                   "_transaction_id_ref": ""
                   }
    # reference to transaction id

    def __init__(self, input_addr: list[str], output_addr: list[str], value: int, precision: int = 4) -> None:
        super().__init__(self._type, self._data)
        self.input_addr = input_addr
        self.output_addr = output_addr
        self.value = value
        self.precision = precision
        self.status = "pending"

    @property
    def input_addr(self) -> str:
        return self.data['input_addr']

    @property
    def output_addr(self) -> str:
        return self.data['output_addr']

    @property
    def value(self) -> int:
        return self.data['value']

    @property
    def type(self) -> RecordType:
        return self._type

    @property
    def precision(self) -> int:
        return self.data['precision']

    @input_addr.setter
    def input_addr(self, val: list[str]):
        try:
            if not val or not isinstance(val, str):
                raise ValueError('empty string or not a string')
        except ValueError:
            raise ValueError('input_addr must be a non-empty string')
        self.data['input_addr'] = val

    @output_addr.setter
    def output_addr(self, val: list[str]):
        try:
            if not val or not isinstance(val, str):
                raise ValueError('empty string or not a string')
        except ValueError:
            raise ValueError('output_addr must be a non-empty string')
        self.data['output_addr'] = val

    @value.setter
    def value(self, val: int):
        try:
            if not val or not isinstance(val, int) or val < 0:
                raise ValueError('empty or zero value or not an int')
        except ValueError:
            raise ValueError('value must be a non-empty int greater than 0')
        self.data['value'] = val

    @precision.setter
    def precision(self, val: int):
        try:
            if not val or not isinstance(val, int) or val < 0:
                raise ValueError('empty or zero value or not an int')
        except ValueError:
            raise ValueError('precision must be an int >= 0')
        self.data['precision'] = val

    def lock_output(self, output_addr: str, )
