from dataclasses import dataclass
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


class TransactionInput():

    # digital signature to be checked by nodes against the public key
    # ~ScriptSig
    digital_signature: str = ""
    # original public key used for the lock in the output
    full_public_key: str = ""

    def __init__(self, transaction_id: str, output_index: int):
        # transaction id to use as source of funds
        self.transaction_id = transaction_id
        # index of the output to use from the transaction
        self.output_index = output_index


class TransactionOutput():
    def __init__(self, value: int, dest_full_pub_key: str):
        # value to spend
        self.value = value
        # lock to be unlocked for spending
        # ~scriptPubKey
        self.hashed_src_pub_key = hash160(dest_full_pub_key)


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
                   "_transaction_id_ref": ""  # reference to transaction id
                   }

    def __init__(self, input_addr: list[TransactionInput], output_addr: list[TransactionOutput]) -> None:
        super().__init__(self._type, self._data)
        self.input_addr = input_addr
        self.output_addr = output_addr

    @property
    def input_addr(self) -> list[TransactionInput]:
        return self.data['input_addr']

    @property
    def output_addr(self) -> list[TransactionOutput]:
        return self.data['output_addr']

    @property
    def type(self) -> RecordType:
        return self._type

    @input_addr.setter
    def input_addr(self, val: list[TransactionInput]) -> None:
        try:
            if not val or not isinstance(val, list) or not all(isinstance(x, TransactionInput) for x in val):
                raise ValueError("Invalid input address")
            self.data['input_addr'] = val
        except ValueError as e:
            print(e)

    @output_addr.setter
    def output_addr(self, val: list[TransactionOutput]) -> None:
        try:
            if not val or not isinstance(val, list) or not all(isinstance(x, TransactionOutput) for x in val):
                raise ValueError("Invalid output address")
            self.data['output_addr'] = val
        except ValueError as e:
            print(e)

    def to_string(self) -> str:
        return super().to_string()
