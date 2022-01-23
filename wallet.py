import ecdsa
from key_pair import KeyPair


class Wallet():
    """
    A class to store (as a wallet) key chain composed of private and public keys
    """

    _key_chain: dict[str, KeyPair] = {}

    def __init__(self, key_pair: list[KeyPair] = None) -> None:
        if key_pair is None:
            key_pair = [KeyPair("default")]
        for kp in key_pair:
            self.add_key_pair(kp)

    def add_key_pair(self, key_pair: KeyPair) -> None:
        """
        Add a known key pair to the key chain of the wallet
        """
        if key_pair.name in self.key_chain:
            key_name = key_pair.name+"_"+str(len(self.key_chain))
            self.key_chain[key_name] = key_pair
            self.key_chain[key_name].name = key_name
            print(f"Key pair {key_name} added")
        else:
            self.key_chain[key_pair.name] = key_pair

    def sign(self, data: str, key_chain_name: str) -> str:
        """
        Sign data with the private key
        """
        private_key = self.key_chain[key_chain_name].private_key
        return private_key.sign(data.encode()).hex()

    def verify(self, data: str, signature: str, key_chain_name: str) -> bool:
        """
        Verify the signature of data with the public key
        """
        public_key = self.key_chain[key_chain_name].public_key
        return public_key.verify(bytes.fromhex(signature), data.encode())

    @property
    def key_chain(self) -> dict[str, KeyPair]:
        """
        Return the key chain of the wallet
        """
        return self._key_chain
