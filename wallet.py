import ecdsa
from ecdsa.util import randrange_from_seed__trytryagain
import binascii
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum


class KeyPair():
    def __init__(self, seed: str = None):
        if seed is None:
            self.seed = Bip39MnemonicGenerator().FromWordsNumber(
                Bip39WordsNum.WORDS_NUM_12).ToStr()
        else:
            self.seed = seed
        self.private_key = self.generate_private_key(self.seed)
        self.public_key = self.generate_public_key()

    def generate_private_key(self, seed: str):
        curve = ecdsa.SECP256k1
        secexp = randrange_from_seed__trytryagain(seed, curve.order)
        return ecdsa.SigningKey.from_secret_exponent(secexp, curve=curve).to_string().hex()

    def generate_public_key(self):
        return ecdsa.VerifyingKey.from_string(bytes.fromhex(self.private_key), curve=ecdsa.SECP256k1).to_string().hex()


class Wallet():
    """
    A class to store the private key and public key of a wallet
    """

    def __init__(self, key_pair: KeyPair = None) -> None:
        self.key_chain: list[KeyPair] = [key_pair] if key_pair else []

    def add_key_pair(self, key_pair: KeyPair) -> None:
        """
        Add a key pair to the wallet
        """
        self.key_chain.append(key_pair)

    def sign(self, data: str, key_chain_index: int = 0) -> str:
        """
        Sign data with the private key
        """
        private_key = ecdsa.SigningKey.from_string(
            self.key_chain[key_chain_index].private_key)
        return private_key.sign(data.encode()).hex()

    def verify(self, data: str, signature: str) -> bool:
        """
        Verify the signature of data with the public key
        """
        public_key = ecdsa.VerifyingKey.from_string(
            bytes.fromhex(self.key_chain[0].public_key))
        return public_key.verify(bytes.fromhex(signature), data.encode())
