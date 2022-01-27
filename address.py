import imp
import base58
from enum import Enum
from crypt_utils import sha256d, checksum, is_checksum_valid, add_checksum, hash160


class AddressPrefixType(Enum):
    P2PKH = b'x00'


class Address(object):
    def __init__(self, full_public_key: str, prefix: AddressPrefixType = AddressPrefixType.P2PKH):
        self._prefix: bytes = prefix.value
        self._hash160 = hash160(full_public_key)
        self._raw_address: bytes = b''.join(
            [self.prefix, add_checksum(self._hash160)])
        self._address_base58: bytes = self.encode_base58(self._raw_address)

    def __str__(self):
        return self._raw_address.decode()

    @classmethod
    def verify(cls, address: bytes) -> bool:
        data = base58.b58decode(address)
        return is_checksum_valid(data)

    @property
    def prefix(self) -> bytes:
        return self._prefix

    @property
    def raw_address(self) -> bytes:
        return self._raw_address

    @property
    def address_base58(self) -> bytes:
        return self._address_base58

    @property
    def public_address(self) -> bytes:
        return self.address_base58

    @classmethod
    def encode_base58(cls, address_to_encode: bytes) -> bytes:
        return base58.b58encode(address_to_encode)

    @classmethod
    def decode_base58(cls, base58_address: bytes) -> bytes:
        return base58.b58decode(base58_address)
