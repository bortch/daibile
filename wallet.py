import ecdsa
from key_pair import KeyPair
from transaction import Transaction, TransactionInput, TransactionOutput


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

    def create_transaction(self, value: int, outputs_addr: list[TransactionOutput],
                           inputs_addr: list[TransactionInput], key_chain_name: str) -> Transaction:
        """
        Create a transaction with the given value and outputs
        """
        src_pub_key = self.key_chain[key_chain_name].public_key.to_string(
        ).hex()
        # source of value to spend
        inputs = []
        # destination of value to send
        outputs = []
        # create inputs
        for input_addr in inputs_addr:
            # select previous transaction as source of funds
            inputs.append(TransactionInput(input_addr.transaction_id,
                                           input_addr.output_index))
        # create outputs
        for output_addr in outputs_addr:
            #
            outputs.append(TransactionOutput(value, src_pub_key))
        transaction = Transaction(inputs, outputs)

        return transaction
