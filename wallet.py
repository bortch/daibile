import ecdsa
from key_pair import KeyPair


class Wallet():
    """
    A class to store the private key and public key of a wallet
    """

    key_chain: dict[str, KeyPair] = {}

    def __init__(self, key_pair: KeyPair = None) -> None:
        if key_pair is None:
            key_pair = KeyPair()
        self.add_key_pair(key_pair)

    def add_key_pair(self, key_pair: KeyPair) -> None:
        """
        Add a known key pair to the key chain of the wallet
        """
        try:
            if self.key_chain[key_pair.name]:
                raise KeyError(f"Key pair {key_pair.name} already exists")
            else:
                self.key_chain[key_pair.name] = key_pair
        except KeyError:
            key_name = key_pair.name+"_"+str(len(self.key_chain))
            self.key_chain[key_name] = key_pair

    def sign(self, data: str, key_chain_name: str) -> str:
        """
        Sign data with the private key
        """
        private_key = ecdsa.SigningKey.from_string(
            self.key_chain[key_chain_name].private_key)
        return private_key.sign(data.encode()).hex()

    def verify(self, data: str, signature: str, key_chain_name: str) -> bool:
        """
        Verify the signature of data with the public key
        """
        public_key = ecdsa.VerifyingKey.from_string(
            bytes.fromhex(self.key_chain[key_chain_name].public_key))
        return public_key.verify(bytes.fromhex(signature), data.encode())
