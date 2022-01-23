import ecdsa
from key_pair import KeyPair


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

    def verify(self, data: str, signature: str, key_chain_index: int = 0) -> bool:
        """
        Verify the signature of data with the public key
        """
        public_key = ecdsa.VerifyingKey.from_string(
            bytes.fromhex(self.key_chain[key_chain_index].public_key))
        return public_key.verify(bytes.fromhex(signature), data.encode())
