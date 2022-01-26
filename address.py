import imp
import base58
from enum import Enum
from crypt_utils import sha256d, checksum, is_checksum_valid, add_checksum


class AddressPrefixType(Enum):
    P2PKH = "00"


class Address(object):
    def __init__(self, full_public_key: str, prefix: AddressPrefixType = AddressPrefixType.P2PKH):
        self._prefix = prefix.value
        self._raw_address = full_public_key
        self._address = self.to_base58()

    def __str__(self):
        return self.address.decode()

    @classmethod
    def verify(cls, address: str):
        data = base58.b58decode(address)
        return is_checksum_valid(data)

    @property
    def prefix(self):
        return self._prefix

    @property
    def raw_address(self):
        return self._raw_address

    @property
    def address(self):
        return self._address

    def to_base58(self):
        return base58.b58encode(self.prefix + add_checksum(self.raw_address))
