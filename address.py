import imp
import base58
from enum import Enum
from crypt_utils import sha256d, checksum, is_checksum_valid, add_checksum


class AddressPrefixType(Enum):
    P2PKH = "00"
    P2SH = "50"


class Address(object):
    def __init__(self, data: str, prefix: AddressPrefixType = AddressPrefixType.P2PKH):
        self._prefix = prefix.value
        self._data = data
        self._address = base58.b58encode(self.prefix + add_checksum(self.data))

    def __str__(self):
        return self.address.decode()

    @classmethod
    def verify(cls, address: str):
        data = base58.b58decode(address)
        return is_checksum_valid(data.decode())

    @property
    def prefix(self):
        return self._prefix

    @property
    def data(self):
        return self._data

    @property
    def address(self):
        return self._address
