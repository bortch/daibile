import ecdsa
from ecdsa.util import randrange_from_seed__trytryagain
from ecdsa import SigningKey, VerifyingKey
import binascii
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum


class KeyPair():

    _seed: str
    _public_key: str
    _private_key: str
    _curve = ecdsa.SECP256k1

    def __init__(self, seed: str = None):
        self._seed = Bip39MnemonicGenerator().FromWordsNumber(
            Bip39WordsNum.WORDS_NUM_12).ToStr() if seed is None else seed
        self._generate_keys(self._seed)

    def _generate_keys(self, seed):
        secexp = randrange_from_seed__trytryagain(seed, self._curve.order)
        priv_key = SigningKey.from_secret_exponent(secexp, curve=self._curve)
        pub_key = priv_key.get_verifying_key()
        self._private_key = priv_key.to_string().hex()
        self._public_key = pub_key.to_string().hex()

    @property
    def seed(self) -> str:
        return self._seed

    @property
    def private_key(self) -> str:
        return self._private_key

    @ property
    def public_key(self) -> str:
        return self._public_key
