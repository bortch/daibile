from os.path import join
import ecdsa
from ecdsa.util import randrange_from_seed__trytryagain
from ecdsa import SigningKey, VerifyingKey
import binascii
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum
from address import Address


class KeyPair():

    _seed: str
    _private_key: SigningKey
    _public_key: VerifyingKey
    _private_key_hex: str
    _public_key_hex: str
    _curve = ecdsa.SECP256k1
    _name: str
    _path: str = "./"
    _address: Address

    def __init__(self,  name: str, seed: str = None, path: str = None):
        self._name = name
        if path is not None:
            self._path = path
        if seed is None:
            self.generate_seed()
        else:
            self._seed = seed
        self._generate_keys(self._seed)
        self._address = Address(self._public_key_hex)

    def _generate_keys(self, seed):
        secexp = randrange_from_seed__trytryagain(seed, self._curve.order)
        # private key
        self._private_key = SigningKey.from_secret_exponent(
            secexp, curve=self._curve)
        priv_key_hex = binascii.hexlify(self._private_key.to_string()).decode()
        self._private_key_hex = priv_key_hex
        # write public key to file
        pk_pem = self._private_key.to_pem()
        with open(join(self._path, f"{self._name}_pk.pem"), "w") as f:
            f.write(pk_pem.decode())
        # derive public key
        pub_key_pem = self._private_key.get_verifying_key().to_pem()
        self._public_key = VerifyingKey.from_pem(pub_key_pem)
        pub_key_hex = binascii.hexlify(self._public_key.to_string()).decode()
        self._public_key_hex = pub_key_hex

    def generate_seed(self):
        self._seed = Bip39MnemonicGenerator().FromWordsNumber(
            Bip39WordsNum.WORDS_NUM_12).ToStr()
        with open(join(self._path, f"{self._name}_seed.txt"), "w") as f:
            f.write(self._seed)

    @property
    def seed(self) -> str:
        return self._seed

    @property
    def private_key_hex(self) -> str:
        return self._private_key_hex

    @property
    def public_key_hex(self) -> str:
        return self._public_key_hex

    @property
    def name(self) -> str:
        return self._name

    @property
    def private_key(self) -> SigningKey:
        return self._private_key

    @property
    def public_key(self) -> VerifyingKey:
        return self._public_key

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def address(self) -> Address:
        return self._address
