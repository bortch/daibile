from dataclasses import dataclass
from crypt_utils import checksum, is_checksum_valid, add_checksum
from crypt_utils import sha256d, hash160
from record_interface import RecordInterface
from record_type import RecordType


class TransactionInput():

    # The digital signature to be checked by nodes against the public key
    # to verify that the claimer is the owner of the locked coins
    # ~ScriptSig
    digital_signature: bytes = b''
    # The original public key used for the lock in the output
    full_public_key: bytes = b''

    def __init__(self, transaction_id: str, output_index: int = 0):
        """This class is used to store the information of a transaction input

        Args:
            transaction_id (str): a hash of the transaction referenced as source of funds
            output_index (int): the index of the output in the transaction referenced as source of funds.
            The default value is 0, which means the first output of the transaction referenced as source of funds.
        """
        # transaction id to use as source of funds
        self.transaction_id = transaction_id
        # index of the output to use from the transaction
        self.output_index = output_index

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "output_index": self.output_index,
            "digital_signature": self.digital_signature,
            "public_key": self.full_public_key
        }

    def to_string(self):
        return str(self.to_dict())


class TransactionOutput():
    """output of a transaction"""

    def __init__(self, value: int, public_address: str | bytes):
        """This object is used to store the value to be sent to a recipient public address

        Args:
            value (int): the value to be sent
            public_address (str): the public address of the recipient. 
            Must be an sha256ed hash of the public key hash160 with a checksum.
            It will be used as lock for the recipient to spend the value.
        """
        # value to spend
        self.value = value
        # lock to be unlocked for spending
        # based on Bitcoin's scriptPubKey
        self.public_address = public_address

    def to_dict(self):
        return {
            "value": self.value,
            "public_address": self.public_address
        }

    def to_string(self):
        return str(self.to_dict())


class TransactionData():
    def __init__(self, inputs: list[TransactionInput], outputs: list[TransactionOutput]):
        self.inputs = inputs
        self.outputs = outputs

    def to_dict(self):
        return {
            "inputs": [input.to_dict() for input in self.inputs],
            "outputs": [output.to_dict() for output in self.outputs]
        }

    def to_string(self):
        return str(self.to_dict())


class Transaction(RecordInterface):

    # type of record
    _type: RecordType = RecordType.TRANSACTION
    # data of a transaction
    _data: dict = {"input_addr": [],  # list of input addresses
                   "output_addr": []}  # list of output addresses

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
        base = super().to_string()+"\n"
        for i in range(len(self.input_addr)):
            base += f"input_addr[{i}] = {self.input_addr[i].to_string()}\n"
        for i in range(len(self.output_addr)):
            base += f"output_addr[{i}] = {self.output_addr[i].to_string()}\n"

        return base
